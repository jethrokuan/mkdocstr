from .yasnippet import yas_transform
import re

_OUTPUT_STYLE_MAPPER = {"yas": yas_transform}


def get_output_style(s: str):
  if s not in _OUTPUT_STYLE_MAPPER:
    raise ValueError(f"Invalid style: {s}")
  return _OUTPUT_STYLE_MAPPER[s]
