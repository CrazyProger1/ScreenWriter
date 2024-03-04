from dataclasses import dataclass

from src.core.types import BaseStyle


@dataclass
class CommonStyle(BaseStyle):
    font: str
    font_size: int
