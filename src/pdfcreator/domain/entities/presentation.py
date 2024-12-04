from dataclasses import dataclass
from typing import List

from pdfcreator.domain.entities.slidedata import SlideData


@dataclass
class Presentation:
    file_path: str
    slides: List['SlideData'] = None