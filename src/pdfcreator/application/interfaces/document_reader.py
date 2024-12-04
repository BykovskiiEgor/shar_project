from abc import ABC, abstractmethod

class DocumentReader(ABC):
    @abstractmethod
    def read(self, file_path:str):
        """Reads a document and returns its content."""
        pass
    
    def read_tables(self, file_path:str):
        """Reads a document and returns its tables content."""
        pass