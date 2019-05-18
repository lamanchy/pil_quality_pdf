from pil_quality_pdf.quality_constants import TRANSFORM_WAY, ROTATE_WAY
from .quality_constants import RESIZE_WAY


def rotate(img, angle, expand=True, center=None, translate=None, fillcolor=None):
  return img.rotate(angle, resample=ROTATE_WAY, expand=expand,
                    center=center, translate=translate, fillcolor=fillcolor)


def transform(img, size, method, data=None, fill=1, fillcolor=None):
  return img.transform(size, method, resample=TRANSFORM_WAY, data=data, fill=fill, fillcolor=fillcolor)


def resize(img, xy, box=None):
    return img.resize(xy, resample=RESIZE_WAY, box=box)
