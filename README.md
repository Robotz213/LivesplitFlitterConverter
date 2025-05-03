# LiveSplit to FlitterSplit Converter

A Python tool to convert LiveSplit's .lss files into FlitterSplit-compatible JSON format.

## Features

- Converts LiveSplit split files (.lss) to FlitterSplit JSON format
- Preserves split names, personal bests, and gold splits
- Handles time formatting and Unicode filename sanitization
- Easy to use command-line interface

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Robotz213/LivesplitFlitterConverter.git
cd LivesplitFlitterConverter
```

2. Install using pip:

```bash
pip install .
```

## Usage

### Command Line

Convert a LiveSplit file using the command line:

```bash
python -m livesplitflitterconverter path/to/your/splits.lss
```

### Python Module

Use the converter in your Python code:

```python
from livesplitflitterconverter import FlitterJson

# Convert a file
FlitterJson("path/to/your/splits.lss")
```

## Output

The converter will create a JSON file in the same directory as your input file, with the same name but a .json extension. The JSON file follows the FlitterSplit format:

```json
{
  "title": "Game Name",
  "category": "Category Name",
  "attempts": 0,
  "completed": 0,
  "split_names": ["Split 1", "Split 2", ...],
  "golds": [
    {"duration": "00:01:23.456"},
    ...
  ],
  "personal_best": {
    "attempt": 0,
    "splits": [
      {"time": "00:01:23.456"},
      ...
    ]
  }
}
```

## Requirements

- Python 3.12 or higher

## License

This project is licensed under the MIT License - see the LICENSE file for details.
