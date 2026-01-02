import cv2

class CameraBase:
    def __init__(self, device_index: int, name: str, angle_deg: float):
        self.device_index = device_index
        self.name = name
        self.angle_deg = angle_deg

        self.cap = cv2.VideoCapture(device_index)
        if not self.cap.isOpened():
            raise RuntimeError(f"{name} could not open index {device_index}")

        # self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        # self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def read(self):
        ret, frame = self.cap.read()
        return frame if ret else None

    def release(self):
        self.cap.release()
