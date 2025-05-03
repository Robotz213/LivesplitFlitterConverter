"""Module for converting LiveSplit files to FlitterSplit JSON format.

This module provides functionality to convert LiveSplit's .lss files into a format
compatible with FlitterSplit. It handles parsing split times, formatting them correctly,
and generating a JSON output file.

Globals:
    json_model (dict): Template for the FlitterSplit JSON structure containing default values
"""

from pathlib import Path
from typing import Dict, Generator, Any
import unicodedata
import xml.etree.ElementTree as ET
import json


"""json

Json Model
{
  "title": "Game Title",
  "category": "Any Category",
  "attempts": 0,
  "completed": 0,
  "split_names": [

  ],
  "golds": [
    {
      "duration": "0.00"
    }
  ],
  "personal_best": {
    "attempt": 0,
    "splits": [
      {
        "time": "0.00"
      }
    ]
  }
}

"""

json_model = {
    "title": "",
    "category": "",
    "attempts": 0,
    "completed": 0,
    "split_names": [],
    "golds": [],
    "personal_best": {"attempt": 0, "splits": []},
}


class FlitterJson:
    """Handles conversion of LiveSplit files to FlitterSplit JSON format.

    This class manages the parsing and conversion of LiveSplit's .lss files into
    FlitterSplit's JSON format. It handles reading split times, best segments,
    and other relevant data.

    Attributes:
        tree (ElementTree): The parsed XML tree from the LiveSplit file.
        root (Element): The root element of the XML tree.
    """

    def parse_time(self, t: str) -> str:
        """Convert a time string to a formatted string with 3-digit milliseconds.

        Args:
            t (str): A time string in the format "HH:MM:SS.microseconds"

        Returns:
            str: A formatted time string with exactly 3 decimal places for milliseconds

        Examples:
            >>> parse_time("00:01:23.4567890")
            "00:01:23.456"
        """
        if "." in t:
            time_part, ms_part = t.split(".", 1)
            trimmed_ms = (ms_part + "000")[:3]
            return f"{time_part}.{trimmed_ms}"
        return t

    def format_string(self, string: str) -> str:
        """Return a secure, normalized filename based on the input string.

        Normalizes Unicode characters and removes any combining characters to create
        a safe filename.

        Args:
            string (str): The original filename to be sanitized

        Returns:
            str: A sanitized version of the filename safe for filesystem use

        Examples:
            >>> format_string("File Name! @#$")
            "File Name"
        """
        return "".join(
            [
                c
                for c in unicodedata.normalize("NFKD", string)
                if not unicodedata.combining(c)
            ]
        )

    def __init__(self, file_input: str):
        """Initialize FlitterJson converter with input file path.

        Creates a new FlitterJson instance and processes the input LiveSplit file,
        generating a JSON output file in the FlitterSplit format.

        Args:
            file_input (str): Path to the LiveSplit .lss file to be converted

        Raises:
            FileNotFoundError: If the input file does not exist
            xml.etree.ElementTree.ParseError: If the input file is not valid XML
        """
        flitter_json: Dict[str, str | int | list[dict[str, str]]] = json_model
        flitter_json["personal_best"]["splits"].clear()
        flitter_json["golds"].clear()
        flitter_json["split_names"].clear()

        for segment in self.generator_segments(file_input):
            if flitter_json["title"] == "" or flitter_json["category"] == "":
                # Set the title and category only once
                flitter_json["title"] = self.root.findtext("GameName")
                flitter_json["category"] = self.root.findtext("CategoryName")

            personal_best = (
                segment.findall("SplitTimes")[0]
                .findall("SplitTime")[0]
                .findall("RealTime")[0]
                .text
            )

            best_segment = (
                segment.findall("BestSegmentTime")[0].findall("RealTime")[0].text
            )

            # Parse the time strings into timedelta objects
            personal_best = self.parse_time(personal_best)
            best_segment = self.parse_time(best_segment)

            flitter_json["split_names"].append(segment.findtext("Name"))
            flitter_json["personal_best"]["splits"].append({"time": str(personal_best)})
            flitter_json["golds"].append({"duration": str(best_segment)})

        filename_output = self.format_string(Path(file_input).name)
        output_json = (
            Path(file_input)
            .parent.resolve()
            .joinpath(filename_output)
            .with_suffix(".json")
        )

        with output_json.open("w") as json_file:
            json.dump(flitter_json, json_file, indent=4)
        print(f"Json file created: {output_json}")

    def generator_segments(self, lss_path: str) -> Generator[ET.Element, Any, None]:
        """Generate segments from LiveSplit file.

        Creates a generator that yields each segment from the LiveSplit file
        for processing.

        Args:
            lss_path (str): Path to the LiveSplit .lss file

        Yields:
            Element: XML Element representing a single segment

        Raises:
            FileNotFoundError: If the lss_path does not exist
            xml.etree.ElementTree.ParseError: If the file is not valid XML
        """
        self.tree = ET.parse(lss_path)
        self.root = self.tree.getroot()

        segments = self.root.findall(".//Segment")
        for segment in segments:
            yield segment

    def convert_lss_to_flitter_json(
        lss_path, output_json_path, title="Game Title", category="Any Category"
    ):
        """convert_lss_to_flitter_json _summary_

        _extended_summary_
        """
