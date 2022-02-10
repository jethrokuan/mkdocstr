from mkdocstr.ttypes import Function
from mkdocstr.langs import FUNCTION_GETTERS
from pathlib import Path


def get_file_extension(file_path: str) -> str:
  """Return file extension for FILE_PATH."""
  return Path(file_path).suffix[1:]


def get_docstring_generator(
  file_path: str,
  style: str,
):
  lang = get_file_extension(file_path)
  function_getter = FUNCTION_GETTERS[lang](file_path)
  style_generator = None
  return function_getter, None
