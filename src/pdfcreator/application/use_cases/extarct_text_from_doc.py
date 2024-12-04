import abc

from pdfcreator.application.dto.documnt import ReadDocumentDTO, DocumentTextDTO
from pdfcreator.application.use_cases.common import UseCase
from pdfcreator.application.interfaces.document_reader import DocumentReader


class ExtractTextFromDocUseCase(UseCase[ReadDocumentDTO, DocumentTextDTO], abc.ABC):
    pass    


class ExtractTextFromDocUseCaseImpl(ExtractTextFromDocUseCase):            
    def __init__(self, document_reader: DocumentReader):
        self.document_reader = document_reader

    async def __call__(self, data: ReadDocumentDTO) -> DocumentTextDTO:        
        document = self.document_reader.read(data.file_path)
        return document