from mkdocstr.ttypes import Function
from mkdocstr.output_styles import get_output_style
from pathlib import Path
from types import FunctionType
import attr

from mako.template import Template


@attr.s
class DocstringGenerator(object):
  lang = attr.ib(type=str, default=None)
  template_file = attr.ib(type=str, default=None)
  output_style = attr.ib(type=FunctionType, default=None)

  def set_lang(self, lang: str):
    self.lang = lang
    return self

  def set_style(self, style: str):
    self.template_file = str(Path("templates") / Path(f"{self.lang}_{style}"))
    return self

  def set_output_style(self, style: str):
    self.output_style = get_output_style(style)
    return self

  def generate(self, fn: Function) -> str:
    templ = Template(filename=self.template_file)
    rendered_template = templ.render(fn=fn)
    converted_template = self.output_style(rendered_template)
    return converted_template
