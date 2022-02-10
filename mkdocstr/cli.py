from argparse import ArgumentParser
from mkdocstr.docstring_generator import get_docstring_generator


def main():
  parser = ArgumentParser("mkdocstr")
  parser.add_argument("file", type=str, help="File to read.")
  parser.add_argument("--loc", type=str, help="Location of code.")
  parser.add_argument("--fn", type=str, help="Function to parse.")

  args = parser.parse_args()

  if args.fn:
    function_getter, _ = get_docstring_generator(args.file, None)
    print(function_getter.get_function_by_name(args.fn))


if __name__ == "__main__":
  main()
