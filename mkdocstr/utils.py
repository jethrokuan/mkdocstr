from pathlib import Path


def get_file_extension(file_path: str) -> str:
  """Return file extension for FILE_PATH."""
  try:
    return Path(file_path).suffix[1:]
  except:
    return ""
