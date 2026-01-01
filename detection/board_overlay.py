import cv2


class BoardOverlay:
    def __init__(self, calib: dict):
        self.ref_w = calib["image_width"]
        self.ref_h = calib["image_height"]

        self.bull = calib["bullseye"]
        self.center = calib["board_center"]

        self.axis_major = calib["axis_major"]
        self.axis_minor = calib["axis_minor"]
        self.rotation = calib["rotation_deg"]

    def draw(self, frame):
        h, w = frame.shape[:2]

        sx = w / self.ref_w
        sy = h / self.ref_h

        center = (
            int(self.center[0] * sx),
            int(self.center[1] * sy)
        )

        bull = (
            int(self.bull[0] * sx),
            int(self.bull[1] * sy)
        )

        axes = (
            int(self.axis_major * sx),
            int(self.axis_minor * sy)
        )

        vis = frame.copy()

        # äußerer Board-Ring
        cv2.ellipse(
            vis,
            center=center,
            axes=axes,
            angle=self.rotation,
            startAngle=0,
            endAngle=360,
            color=(0, 255, 0),
            thickness=2
        )

        # Bullseye (radius proportional)
        bull_radius = int(min(axes) * 0.05)
        cv2.circle(vis, bull, bull_radius, (0, 0, 255), 2)

        # Center
        cv2.circle(vis, center, 4, (255, 0, 0), -1)

        return vis
