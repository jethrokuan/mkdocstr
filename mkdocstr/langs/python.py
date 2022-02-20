from tree_sitter import Parser
from tree_sitter import Language
from mkdocstr.ttypes import FunctionGetter, Function, Parameter
from mkdocstr.tree_utils import find_node_in_tree

_PY_LANGUAGE = Language("mkdocstr/languages.so", "python")

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
    def matcher(node):
      return (
        node.type == "function_definition"
        and node.children[1].text.decode("utf-8") == fn_name
      )

    tree = self.parser.parse(bytes(self.contents, "utf-8"))
    cursor = tree.walk()
    find_node_in_tree(cursor, matcher)
    if cursor.node == tree.root_node:
      return None
    name_node = cursor.node.children[1]
    name = name_node.text.decode("utf-8")
    parameters_node = cursor.node.children[2]
    parameters = [self._node_to_parameter(n) for n in parameters_node.children]
    parameters = list(filter(lambda n: n is not None, parameters))
    return Function(name=name, parameters=parameters)

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
