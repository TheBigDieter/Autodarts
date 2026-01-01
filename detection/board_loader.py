import json
from pathlib import Path
from detection.board_overlay import BoardOverlay


def load_board_overlays(path="config/board_calibration.json"):
    with open(Path(path)) as f:
        data = json.load(f)

    return {k: BoardOverlay(v) for k, v in data.items()}
