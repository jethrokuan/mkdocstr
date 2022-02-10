"""Build languages.so file."""

from tree_sitter import Language
from pathlib import Path


LANGUAGES = list(Path("langs").iterdir())

BUILD_OUTPUT = "build/languages.so"

Path("build").mkdir(exist_ok=True)

Language.build_library(
  # Store the library in the `build` directory
  "build/languages.so",
  # Include one or more languages
  LANGUAGES,
)
