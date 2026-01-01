import json
from pathlib import Path
from cameras.camera_20 import Camera20
from cameras.camera_16 import Camera16
from cameras.camera_15 import Camera15

CONFIG = Path("camera_map.json")

def init_cameras():
    if not CONFIG.exists():
        raise RuntimeError("camera_map.json fehlt – erst camera_mapper.py ausführen")

    with open(CONFIG) as f:
        m = json.load(f)

    return (
        Camera20(m["20"]),
        Camera16(m["16"]),
        Camera15(m["15"]),
    )
