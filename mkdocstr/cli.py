from argparse import ArgumentParser
from mkdocstr.docstring_generator import DocstringGenerator
from mkdocstr.langs import get_function_getter
from mkdocstr.ttypes import Parameter, Function
from mkdocstr.utils import get_file_extension


def main():
  parser = ArgumentParser("mkdocstr")
  parser.add_argument("file", type=str, help="File to read.")
  # parser.add_argument("--loc", type=str, help="Location of code.")
  parser.add_argument("--fn", type=str, help="Function to parse.")
  parser.add_argument("--style", type=str, help="Docstring style.", default="google")
  parser.add_argument("--output_style", type=str, help="Output style.", default="yas")

  args = parser.parse_args()

  lang = get_file_extension(args.file)
  function_getter_cls = get_function_getter(lang)
  function_getter = function_getter_cls(args.file)

  function = function_getter.get_function_by_name(args.fn)
  docstring_generator = (
    DocstringGenerator()
    .set_lang(lang)
    .set_style(args.style)
    .set_output_style(args.output_style)
  )
  docstr = docstring_generator.generate(function)
  print(docstr)


if __name__ == "__main__":
  main()
