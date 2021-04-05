import functools
import os

from PIL import ImageFont

from pil_quality_pdf.quality_constants import FONT
from pil_quality_pdf.rendering import mm_to_px
from .quality_constants import ANTIALIASING, RESOLUTION_DPI

import pathlib

@functools.lru_cache(None)
def get_font(size, font=FONT):
    size = int(size * RESOLUTION_DPI * ANTIALIASING // 100)
    try:
        return ImageFont.truetype(os.path.join(pathlib.Path(__file__).parent.absolute(), font), size=size)
    except OSError:
        return ImageFont.truetype(os.path.join(pathlib.Path(__file__).parent.absolute(), FONT), size=size)


def get_max_font_size(draw, text, max_width, max_height, max_font_size, min_font_size=1):
    font_size = max_font_size

    problems = []
    while True:
        size = draw.textsize(text, get_font(font_size), spacing=mm_to_px(font_size / 15.))

        width_ok = max_width is None or size[0] <= max_width
        height_ok = max_height is None or size[1] <= max_height
        if (width_ok and height_ok) or font_size <= min_font_size:
            return font_size, problems

        if width_ok and "width" in problems:
            problems.remove("width")

        if not width_ok and "width" not in problems:
            problems.append("width")

        if height_ok and "height" in problems:
            problems.remove("height")

        if not height_ok and "height" not in problems:
            problems.append("height")

        font_size -= 1
