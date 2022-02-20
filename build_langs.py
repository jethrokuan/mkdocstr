"""Build languages.so file."""

from tree_sitter import Language
from pathlib import Path


def _is_tree_sitter_lang(path: Path):
  return str(path.name).startswith("tree-sitter-")


LANGUAGES = list(filter(_is_tree_sitter_lang, Path("langs").iterdir()))

BUILD_OUTPUT = "mkdocstr/languages.so"

Language.build_library(
  BUILD_OUTPUT,
  LANGUAGES,
)
