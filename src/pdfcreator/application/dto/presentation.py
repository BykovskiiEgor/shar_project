from dataclasses import dataclass
from typing import List


@dataclass
class PresentationTextDTO:
    text: List[str]    
    
    

@dataclass
class ReadPrsDTO:
    file_path:str