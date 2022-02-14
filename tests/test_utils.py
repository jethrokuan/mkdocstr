from mkdocstr.utils import get_file_extension


def test_get_file_extension():
  assert get_file_extension("abc.py") == "py"
  assert get_file_extension("abc.js") == "js"
  assert get_file_extension("abc.jsx") == "jsx"
