import argparse
from datetime import date

from ..infrastructure.database import WeightRecord, Database
from .validation import validate_weight

class Handler:

    def __init__(self, db: Database):
        self.database = db

    def handle(self, args: argparse.Namespace):
    
        if args.command == "add":
            self._handle_add(args)
        elif args.command == "show":
            self._handle_show(args)
        elif args.command == "clean":
            self._handle_clean(args)

    def _handle_add(self, args):
        weight = validate_weight(args.weight)
        day =  date.today()
        with self.database:
            self.database.add(WeightRecord(day, weight))
            

    def _handle_show(self, args):
        pass

    def _handle_clean(self, args):
        pass
