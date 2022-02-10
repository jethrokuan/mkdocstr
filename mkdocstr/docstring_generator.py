from mkdocstr.ttypes import Function
from mkdocstr.langs import FUNCTION_GETTERS


def get_docstring_generator(lang: str, style: str, file_path: str):
  function_getter = FUNCTION_GETTERS[lang](file_path)
  style_generator = None
  return function_getter, None
