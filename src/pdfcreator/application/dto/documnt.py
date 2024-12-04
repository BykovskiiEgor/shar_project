from dataclasses import dataclass
from typing import List


@dataclass
class DocumentTextDTO:
    text: List[str]    
    
    

@dataclass
class ReadDocumentDTO:
    file_path:str