from pathlib import Path

# Proje kökü: .../data-sellers
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

def get_data_dir() -> Path:
    """
    Return path to the local data directory.
    (Some challenges download/copy data here.)
    """
    return DATA_DIR
