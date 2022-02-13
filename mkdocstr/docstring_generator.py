from mkdocstr.ttypes import Function
from mkdocstr.langs import FUNCTION_GETTERS
from pathlib import Path
import attr

from mako.template import Template


@attr.s
class DocstringGenerator(object):
  lang = attr.ib(type=str, default=None)
  template_file = attr.ib(type=str, default=None)
  generated_style = attr.ib(type=str, default="yas")

  def set_lang(self, lang: str):
    self.lang = lang
    return self

  def set_style(self, style: str):
    self.template_file = str(Path("templates") / Path(f"{self.lang}_{style}"))
    return self

  def generate(self, fn: Function) -> str:
    templ = Template(filename=self.template_file)
    return templ.render(fn=fn)


def get_file_extension(file_path: str) -> str:
  """Return file extension for FILE_PATH."""
  return Path(file_path).suffix[1:]


def get_function_getter(file_path: str):
  lang = get_file_extension(file_path)
  function_getter = FUNCTION_GETTERS[lang](file_path)
  return function_getter


def get_docstring_generator(file_path: str, style: str):
  lang = get_file_extension(file_path)
  return DocstringGenerator().set_lang(lang).set_style(style)
