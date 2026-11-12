from .config import get_database_path
from .presentation.parser import get_args
from .core.handler import Handler
from .infrastructure.database import Database

def main() -> None:
    db_path = get_database_path()
    if not db_path.exists():
        db_path.parent.mkdir(parents=True, exist_ok=True)
        db_path.touch()

    db = Database(db_path)

    handler = Handler(db)

    args = get_args()

    try:
        handler.handle(args)
    except ValueError as exc:
        print(f"Error: {exc}")
