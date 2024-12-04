import abc

from pdfcreator.application.dto.documnt import ReadDocumentDTO, DocumentTextDTO
from pdfcreator.application.use_cases.common import UseCase
from pdfcreator.application.interfaces.document_reader import DocumentReader


class ExtractTextFromTablesUseCase(UseCase[ReadDocumentDTO, DocumentTextDTO], abc.ABC):
    pass    


class ExtractTextFromTablesUseCaseImpl(ExtractTextFromTablesUseCase):            
    def __init__(self, document_reader: DocumentReader):
        self.document_reader = document_reader

    async def __call__(self, data: ReadDocumentDTO) -> DocumentTextDTO:        
        document = self.document_reader.read_tables(data.file_path)
        return document