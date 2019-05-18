from PIL import Image

RESAMPLE_WAY = Image.BILINEAR  # Image.BICUBIC
RESIZE_WAY = Image.ANTIALIAS  # Image.ANTIALIAS

RESOLUTION_DPI = 300
ANTIALIASING = 3

FONT = "fonts/DejaVuSansMono.ttf"

try:
    from .local_quality_constants import *
except ImportError:
    pass
