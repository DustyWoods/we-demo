import argparse
from importlib.metadata import version

def _create_parser():
    parser = argparse.ArgumentParser(
        description="Weight Tracking Tool"
    )

    PACKAGE_NAME = "we-demo"

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version(PACKAGE_NAME)}"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    add_parser = subparsers.add_parser(
        "add",
        help="Add today's weight record (kg; rounded to one decimal place)"
    )
    add_parser.add_argument(
        "weight",
        type=float
    )

    subparsers.add_parser(
        "show",
        help="Display the past 30 days of weight records using a line chart"
    )

    clean_parser = subparsers.add_parser(
        "clean",
        help="Clear all weight records"
    )
    clean_parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="CLear all weight records without confirmation"
    )

    return parser

def get_args():
    parser = _create_parser()
    args = parser.parse_args()

    return args
