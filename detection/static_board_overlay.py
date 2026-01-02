import cv2


class StaticBoardOverlay:
    def __init__(
        self,
        bull_x, bull_y,
        board_cx, board_cy,
        axis_major, axis_minor,
        rotation_deg
    ):
        self.bull = (int(bull_x), int(bull_y))

        # EXAKT wie im alten StaticBoardDetector
        self.ellipse = (
            (int(board_cx), int(board_cy)),          # center
            (float(axis_major), float(axis_minor)),  # FULL axes lengths!
            float(rotation_deg)
        )

    def draw(self, frame):
        # Bullseye
        cv2.circle(frame, self.bull, 6, (0, 255, 255), -1)

        # äußerer Board-Ring
        cv2.ellipse(frame, self.ellipse, (0, 255, 0), 2)

        return frame
