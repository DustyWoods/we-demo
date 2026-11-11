import argparse

from ..infrastructure.database import Database

class Handler:

    def __init__(self, db: Database):
        self.repository = db

    def handle(self, args: argparse.Namespace):
    
        if args.command == "add":
            self._handle_add(args)
        elif args.command == "show":
            self._handle_show(args)
        elif args.command == "clean":
            self._handle_clean(args)

    def _handle_add(self, args):
        pass

    def _handle_show(self, args):
        pass

    def _handle_clean(self, args):
        pass
