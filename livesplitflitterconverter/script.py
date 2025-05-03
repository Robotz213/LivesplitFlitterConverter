"""Main script module for LiveSplit to FlitterSplit conversion.

This module provides the main entry point for converting LiveSplit files
to FlitterSplit JSON format.
"""

from livesplitflitterconverter import FlitterJson


def main(lss_path: str) -> None:
    """Convert a LiveSplit file to FlitterSplit JSON format.

    Args:
        lss_path (str): Path to the LiveSplit .lss file to be converted

    Raises:
        FileNotFoundError: If the input file does not exist
        xml.etree.ElementTree.ParseError: If the input file is not valid XML
    """
    FlitterJson(lss_path)
