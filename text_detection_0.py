"""It works!

Had to do a simple ``pacman -Syu tesseract tesseract-data-eng`` to
get it installed in WSL but we're all set up!
"""
import pytesseract

from PIL import Image


def ocr_core(filename):
    return pytesseract.image_to_string(Image.open(filename))


print(ocr_core('./ocr_image_1.png'))
