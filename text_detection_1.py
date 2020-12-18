"""It works!

Had to do a simple ``pacman -Syu tesseract tesseract-data-eng`` to
get it installed in WSL but we're all set up!

Added argparse for reproducible use.
"""
import argparse
import sys
from pathlib import Path

import pytesseract
from PIL import Image


def _parse_arguments() -> argparse.Namespace:
    """Parse arguments given by the user.

    Returns
    -------
    args : :class:`argparse.NameSpace()`
        Arguments provided by the user and handled by argparse.

    """
    parser = argparse.ArgumentParser(
        prog="OCR recognition",
        description="Take a picture and return the text in the picture",
    )

    parser.add_argument(
        "input", help="Picture to parse.",
    )

    if len(sys.argv[1:]) == 0:
        parser.print_help()
        sys.exit()

    args = parser.parse_args()
    return args


def ocr_core(filename):
    return pytesseract.image_to_string(Image.open(filename))


def main():
    args = _parse_arguments()

    if not Path(args.input).exists():
        raise FileNotFoundError(args.input)

    text = ocr_core(args.input)
    print(text)
    return text

if __name__ == '__main__':
    main()
