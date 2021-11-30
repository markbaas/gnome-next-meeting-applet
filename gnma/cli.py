"""Console script for gnome_next_meeting_applet."""
import argparse
import sys

import gnma.applet as gnma


def parse_args():
    parser = argparse.ArgumentParser(description="Gnome next meeting applet")
    parser.add_argument("--verbose",
                        "-v",
                        dest="verbose",
                        action="store_true",
                        help="verbose")
    return parser.parse_args()


def cli():
    """Console script for gnome_next_meeting_applet."""
    gnma.run(parse_args())
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover