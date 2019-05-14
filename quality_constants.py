from PIL import Image

RESAMPLE_WAY = Image.BILINEAR  # Image.BICUBIC
RESIZE_WAY = Image.NEAREST  # Image.ANTIALIAS

FONT = "fonts/DejaVuSansMono.ttf"

try:
    from .local_quality_constants import *
except ImportError:
    pass
