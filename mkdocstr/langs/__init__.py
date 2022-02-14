from .python import PythonGetter
from mkdocstr.ttypes import FunctionGetter

FUNCTION_GETTERS = {"py": PythonGetter, "python": PythonGetter}


def get_function_getter(lang: str) -> FunctionGetter:
  return FUNCTION_GETTERS[lang]
