from dataclasses import dataclass
from abc import ABC, abstractmethod
from pathlib import Path

import attr
from typing import List


@dataclass
class Parameter:
  name: str
  default_value: str = None
  type: str = None


@dataclass
class Function:
  name: str
  parameters: List[Parameter]


class FunctionGetter(ABC):
  @abstractmethod
  def get_function_by_name(self, fn_name) -> Function:
    pass

  @abstractmethod
  def get_function_by_loc(self, loc) -> Function:
    pass


@dataclass
class Location:
  x: int
  y: int
