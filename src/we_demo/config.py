from pathlib import Path
from platformdirs import user_data_dir

APP_NAME="we-demo"

def get_database_path():
    return Path(user_data_dir(APP_NAME)) / "weight.db"
