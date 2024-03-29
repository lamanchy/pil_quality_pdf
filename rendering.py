import os
import shutil
from datetime import datetime
from pathlib import Path

import img2pdf
from PIL import Image

from .quality_constants import ANTIALIASING, RESOLUTION_DPI


def do_antialiasing(img):
    if ANTIALIASING == 1:
        return img
    return img.resize((int(img.size[0] / ANTIALIASING), int(img.size[1] / ANTIALIASING)), Image.ANTIALIAS)


def save(path, img):
    img.save(path, optimize=True, dpi=(RESOLUTION_DPI, RESOLUTION_DPI))


class PdfWriter(object):
    def __init__(self, name):
        self.name = name
        self.is_in = False
        self.counter = 0

    def dirname(self):
        return Path('pdf_writer') / f"{self.name}_dir"

    def get_png_path(self, i):
        return os.path.join(self.dirname(), f"{i:09}" + ".png")

    def write(self, img):
        if not self.is_in:
            raise RuntimeError("not in")

        img = do_antialiasing(img)

        path = self.get_png_path(self.counter)
        self.counter += 1
        # print(datetime.now(), "Saving %s. page of file %s" % (self.counter, self.name))
        img.save(path, optimize=True, dpi=(RESOLUTION_DPI, RESOLUTION_DPI))

    def __enter__(self):
        self.counter = 0
        self.is_in = True
        try:
            shutil.rmtree(self.dirname(), ignore_errors=True)
        except FileNotFoundError:
            pass
        self.dirname().mkdir(parents=True)
        try:
            os.remove(self.name + ".pdf")
        except FileNotFoundError:
            pass

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            return
        self.is_in = False

        images = [self.get_png_path(i) for i in range(self.counter)]

        if len(images):
            path = Path('pdfs')
            path.mkdir(parents=True, exist_ok=True)
            with open(path / (self.name + ".pdf"), "wb") as f:
                f.write(img2pdf.convert(images))


def show(img):
    do_antialiasing(img).show()


def mm_to_px(*args):
    x = args
    if len(args) == 1:
        x = args[0]
    if isinstance(x, int) or isinstance(x, float):
        return int(RESOLUTION_DPI * ANTIALIASING * 0.03937 * x)

    return type(x)([mm_to_px(i) for i in x])


def px_to_mm(*args):
    x = args
    if len(args) == 1:
        x = args[0]
    if isinstance(x, int) or isinstance(x, float):
        return x / (RESOLUTION_DPI * ANTIALIASING * 0.03937)

    return type(x)([px_to_mm(i) for i in x])
