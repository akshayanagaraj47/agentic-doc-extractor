from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from typing import Optional, List

def extract_text_from_image(image: Image.Image) -> Optional[str]:
    """Extract text from a PIL image using Tesseract OCR."""
    try:
        return pytesseract.image_to_string(image)
    except Exception:
        return None


def extract_text_from_pdf(pdf_bytes: bytes) -> List[str]:
    """Extract text from each page of a PDF (returns list of page texts)."""
    texts: List[str] = []
    try:
        images = convert_from_bytes(pdf_bytes)
        for img in images:
            text = pytesseract.image_to_string(img)
            texts.append(text)
    except Exception:
        texts.append("")
    return texts
