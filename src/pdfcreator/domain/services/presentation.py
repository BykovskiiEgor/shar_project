from pdfcreator.domain.dto.presentation import PresentationInputDTO
from pptx import Presentation

class PresentationService:
    def validate_format(self, presentation: PresentationInputDTO):
        """Check presentation format"""
        if not presentation.file_path.endswith('.pptx'):
            raise ValueError("Invalid presentation format. Only .pptx files are supported.")
       
       
    def validate_structure(self, presentation: PresentationInputDTO):
        """Checks that file is not empty"""
        if not self.__has_slides(presentation):
            raise ValueError("pptx is empty")
       
       
    def __has_slides(self, presentation: PresentationInputDTO) -> bool:
        """Check if presentation has slides"""
        prs = Presentation(presentation.file_path)
        return len(prs.slides) > 0
    
        