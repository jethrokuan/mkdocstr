from mkdocstr.docstring_generator import get_docstring_generator
from mkdocstr.ttypes import Parameter, Function


def test_get_function_by_name():
  TEST_FILE_PATH = "test_files/python.py"
  function_getter, styler = get_docstring_generator(
    lang="python", style="google", file_path=TEST_FILE_PATH
  )
  function = function_getter.get_function_by_name("a")
  assert function == Function(
    name="a",
    parameters=[
      Parameter(name="arg1"),
      Parameter(name="arg2", default_value="False"),
      Parameter(name="arg3", default_value="0", type="int"),
    ],
  )

  function = function_getter.get_function_by_name("does_not_exist")
  assert function is None
