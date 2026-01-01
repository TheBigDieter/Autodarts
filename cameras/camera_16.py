from cameras.camera_base import CameraBase

class Camera16(CameraBase):
    def __init__(self, idx): super().__init__(idx, "Camera_16", 120.0)
