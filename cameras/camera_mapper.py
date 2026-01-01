import cv2
import json
from pathlib import Path

CONFIG = Path("camera_map.json")

# Maximal 4 Kameras laut deiner Hardware
MAX_INDEX = 4


def find_cameras():
    cams = []

    for i in range(MAX_INDEX):
        cap = cv2.VideoCapture(i, cv2.CAP_MSMF)  # stabil unter Windows
        if not cap.isOpened():
            cap.release()
            continue

        ret, frame = cap.read()
        if ret:
            cams.append(i)

        cap.release()

    return cams


def map_cameras():
    cams = find_cameras()

    if not cams:
        raise RuntimeError("Keine Kameras gefunden")

    mapping = {}

    print("\nFenster anklicken und Taste drücken:")
    print("  2 = Kamera über 20")
    print("  6 = Kamera über 16")
    print("  5 = Kamera über 15")
    print("  f = Frontkamera (ignorieren)")
    print("  ESC = abbrechen\n")

    for idx in cams:
        cap = cv2.VideoCapture(idx, cv2.CAP_MSMF)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow(f"Kamera Index {idx}", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == 27:  # ESC
                cap.release()
                cv2.destroyAllWindows()
                return

            if key in (50, 54, 53, 102):  # 2,6,5,f
                if key == 50:
                    mapping["20"] = idx
                elif key == 54:
                    mapping["16"] = idx
                elif key == 53:
                    mapping["15"] = idx
                elif key == 102:
                    pass  # Frontkamera ignorieren

                cv2.destroyWindow(f"Kamera Index {idx}")
                break

        cap.release()

    if not all(k in mapping for k in ("20", "16", "15")):
        raise RuntimeError("Nicht alle Dartkameras wurden zugeordnet")

    with open(CONFIG, "w") as f:
        json.dump(mapping, f, indent=2)

    cv2.destroyAllWindows()
    print("Mapping gespeichert:", mapping)


if __name__ == "__main__":
    map_cameras()
