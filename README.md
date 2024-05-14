# vbe-decoder
- Python utility script to decode encoded VB files (.vbe)
- Original tool from [here](https://github.com/JohnHammond/vbe-decoder)
- Refactored to avoid translation errors for invalid UTF-8 byte sequences and provide additional error handling logic for `UnicodeDecodeError` exceptions.

# Installation

```bash
# using pipx (recommended)
pipx install git+https://github.com/Mercury0/vbe-decoder.git
```

# Usage

```
usage: vbe-decoder [-h] [-o output] file [file ...]

Decode an encoded VBScript, often seen as a .vbe file

positional arguments:
  file                  file to decode

optional arguments:
  -h, --help            show this help message and exit
  -o output, --output output
                        output file (default stdout)
```
