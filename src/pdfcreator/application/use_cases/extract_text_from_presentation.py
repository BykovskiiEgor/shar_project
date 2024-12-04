import abc

from pdfcreator.application.dto.presentation import ReadPrsDTO, PresentationTextDTO
from pdfcreator.application.use_cases.common import UseCase
from pdfcreator.application.interfaces.presentation_reader import PresentationReader


class ExtractTextFromPrsUseCase(UseCase[ReadPrsDTO, PresentationTextDTO], abc.ABC):
    pass    


class ExtractTextFromPrsUseCaseImpl(ExtractTextFromPrsUseCase):            
    def __init__(self, presentation_reader: PresentationReader):
        self.presentation_reader = presentation_reader

    async def __call__(self, data: ReadPrsDTO) -> PresentationTextDTO:        
        prs = self.presentation_reader.read(data.file_path)
        return prs