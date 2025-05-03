"""Command-line interface for LiveSplit to FlitterSplit converter.

This module provides the command-line interface for converting LiveSplit files
to FlitterSplit JSON format. It handles argument parsing and error reporting.
"""

import traceback
from livesplitflitterconverter.script import main as main_script
import argparse
import sys

if __name__ == "__main__":
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
        main_script(args.input_file)

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
