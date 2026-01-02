import json
from detection.static_board_overlay import StaticBoardOverlay


def load_board_overlays(path="config/board_calibration.json"):
    with open(path) as f:
        data = json.load(f)

    overlays = {}
    for key, c in data.items():
        overlays[key] = StaticBoardOverlay(
            bull_x=c["bullseye"][0],
            bull_y=c["bullseye"][1],
            board_cx=c["board_center"][0],
            board_cy=c["board_center"][1],
            axis_major=c["axis_major"],
            axis_minor=c["axis_minor"],
            rotation_deg=c["rotation_deg"],
        )

    return overlays
