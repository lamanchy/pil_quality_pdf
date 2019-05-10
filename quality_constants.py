from PIL import Image

HIGH_QUALITY = False
# RESAMPLE_WAY = Image.BICUBIC
# RESIZE_WAY = Image.ANTIALIAS
RESOLUTION_DPI = 300
ANTIALIASING = 3

RESAMPLE_WAY = Image.BILINEAR
RESIZE_WAY = Image.NEAREST

FONT = "fonts/DejaVuSansMono.ttf"

try:
    from .local_quality_constants import *
except ImportError:
    pass