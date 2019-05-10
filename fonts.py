import functools

from PIL import ImageFont

from pil_quality_pdf.quality_constants import FONT
from .quality_constants import ANTIALIASING, RESOLUTION_DPI


@functools.lru_cache(None)
def get_font(size, font=FONT):
    return ImageFont.truetype(font, size=int(size * RESOLUTION_DPI * ANTIALIASING / 100))
