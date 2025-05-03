"""Main script module for LiveSplit to FlitterSplit conversion.

This module provides the main entry point for converting LiveSplit files
to FlitterSplit JSON format.
"""

import argparse
import sys
import traceback
from livesplitflitterconverter import FlitterJson


def main(lss_path: str | None = None) -> None:
    """Convert a LiveSplit file to FlitterSplit JSON format.

    Args:
        lss_path (str): Path to the LiveSplit .lss file to be converted

    Raises:
        FileNotFoundError: If the input file does not exist
        xml.etree.ElementTree.ParseError: If the input file is not valid XML
    """
    if lss_path is None:
        try:
            parser = argparse.ArgumentParser(
                description="Convert LiveSplit .lss files to JSON."
            )
            parser.add_argument(
                "input_file",
                metavar="input_file",
                type=str,
                help="Path to the input .lss file.",
            )

            args = parser.parse_args(sys.argv[1:])
            lss_path = args.input_file

        except SystemExit as e:
            err = traceback.format_exception(e)
            msg_list = []
            for line in err:
                if (
                    line.strip().startswith("Traceback")
                    or line.strip().startswith("File")
                    or line.strip().startswith("During")
                    or line.strip().startswith("SystemExit")
                ):
                    continue

                msg_list.append(line.strip())

            msg = "".join(msg_list)
            print(msg)

    FlitterJson(lss_path)
