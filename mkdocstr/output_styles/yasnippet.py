"""Output style for yasnippet."""
from .base import PLACEHOLDER_MATCHER
import re

yas_idx = 0


def yas_transform(s: str):
  def replacer(m):
    global yas_idx
    yas_idx += 1
    return "${" + f"{yas_idx}:{m.group(1)}" + "}"

  return re.sub(PLACEHOLDER_MATCHER, replacer, s)
