from tree_sitter import Parser
from tree_sitter import Language
from mkdocstr.ttypes import FunctionGetter, Function, Parameter

_PY_LANGUAGE = Language("build/languages.so", "python")

_PYTHON_PARSER = Parser()
_PYTHON_PARSER.set_language(_PY_LANGUAGE)


def pairwise(ls):
  a = iter(ls)
  return zip(a, a)


class PythonGetter(FunctionGetter):
  def __init__(self, file_path):
    self.parser = _PYTHON_PARSER
    self.language = _PY_LANGUAGE
    with open(file_path) as f:
      self.contents = f.read()

  def get_function_by_name(self, fn_name: str) -> Function:
    # TODO: Do a proper tree walk to get name
    tree = self.parser.parse(bytes(self.contents, "utf-8"))
    query = self.language.query(
      """
(function_definition
  name: (identifier) @name
  parameters: (parameters) @parameters)
"""
    )
    captures = query.captures(tree.root_node)
    for (name, _), (parameters, _) in pairwise(captures):
      name = name.text.decode("utf-8")
      if name != fn_name:
        continue
      parameters = [self._node_to_parameter(n) for n in parameters.children]
      parameters = list(filter(lambda n: n is not None, parameters))
      return Function(name=name, parameters=parameters)
    else:
      return None

  def get_function_by_loc(self, file_path: str, loc: str) -> Function:
    return None

  def _node_to_parameter(self, node) -> Parameter:
    "Converts a node to parameter."
    if node.type == "identifier":
      return Parameter(name=node.text.decode("utf-8"))
    elif node.type == "default_parameter":
      identifier, _, default_value = node.children
      return Parameter(
        name=identifier.text.decode("utf-8"),
        default_value=default_value.text.decode("utf-8"),
      )
    elif node.type == "typed_default_parameter":
      identifier, _, node_type, _, default_value = node.children
      return Parameter(
        name=identifier.text.decode("utf-8"),
        default_value=default_value.text.decode("utf-8"),
        type=node_type.text.decode("utf-8"),
      )
    else:
      return None
