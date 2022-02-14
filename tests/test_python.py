from mkdocstr.docstring_generator import DocstringGenerator
from mkdocstr.langs import get_function_getter
from mkdocstr.ttypes import Parameter, Function
from mkdocstr.utils import get_file_extension


def test_python_get_function_by_name():
  TEST_FILE_PATH = "test_files/python.py"
  lang = get_file_extension(TEST_FILE_PATH)
  function_getter_cls = get_function_getter(lang)
  function_getter = function_getter_cls(TEST_FILE_PATH)

  docstring_generator = (
    DocstringGenerator().set_lang(lang).set_style("google").set_output_style("yas")
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

  docstr = docstring_generator.generate(function)
  assert docstr == "abc"

  function = function_getter.get_function_by_name("does_not_exist")
  assert function is None
