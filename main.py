import cv2
from cameras.camera_manager import init_cameras
from detection.board_loader import load_board_overlays

cam20, cam16, cam15 = init_cameras()
overlays = load_board_overlays()

camera_map = {
    "Top (20)": (cam20, overlays["20"]),
    "Left (120°)": (cam16, overlays["16"]),
    "Right (240°)": (cam15, overlays["15"]),
}

while True:
    for name, (cam, overlay) in camera_map.items():
        frame = cam.read()
        if frame is None:
            continue

        frame = overlay.draw(frame)
        cv2.imshow(name, frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam20.release()
cam16.release()
cam15.release()
cv2.destroyAllWindows()
