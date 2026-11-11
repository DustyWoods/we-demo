from .config import get_database_path
from .presentation.parser import get_args
from .core.handler import Handler
from .infrastructure.database import Database

def main() -> None:
    db_path = get_database_path()

    db = Database(db_path)

    handler = Handler(db)

    args = get_args()

    handler.handle(args)
