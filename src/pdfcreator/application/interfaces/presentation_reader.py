from abc import ABC, abstractmethod

class PresentationReader(ABC):
    @abstractmethod
    def read(self, file_path:str):
        """Reads a document and returns its content."""
        pass
        