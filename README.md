# LiveSplit to FlitterSplit Converter

A Python tool to convert LiveSplit's .lss files into FlitterSplit-compatible JSON format.

## Features

- Converts LiveSplit split files (.lss) to FlitterSplit JSON format
- Preserves split names, personal bests, and gold splits
- Handles time formatting and Unicode filename sanitization
- Easy to use command-line interface

### Installation

1. Download your split file (e.g., [therun.gg](https://therun.gg/vitroncio/Super%20Mario%2064/120%20Star))
2. Download the _.whl_ file in [Releases](https://github.com/Robotz213/LivesplitFlitterConverter/releases/latest)

   > or build it yourself using [Poetry](https://python-poetry.org/docs/#installation).

3. In the file directory, install using [Pipx (Recommended)](https://pipx.pypa.io/stable/installation)

```bash
# Example:
pipx install livesplitflitterconverter-0.1.0-py3-none-any.whl
```

4. Run it!

```bash
# Example:
livesplitflitterconverter Super+Mario+64-120+Star+Vitroncio.lss
>> Json file created: /home/robotz213/Documents/Super+Mario+64-120+Star+Vitroncio.json

flitter /home/robotz213/Documents/Super+Mario+64-120+Star+Vitroncio.json
```

[Example](https://github.com/user-attachments/assets/fed992e2-99f0-405f-92cc-9b21eac17669)

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
