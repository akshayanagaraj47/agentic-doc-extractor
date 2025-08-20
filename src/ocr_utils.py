from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from typing import Optional, List
import shutil

# 🔹 Auto-detect tesseract binary path (works on Streamlit Cloud & local)
tess_bin = shutil.which("tesseract")
if tess_bin:
    pytesseract.pytesseract.tesseract_cmd = tess_bin


def extract_text_from_image(image: Image.Image) -> Optional[str]:
    """Extract text from a PIL image using Tesseract OCR."""
    try:
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"Error extracting text from image: {e}"


def extract_text_from_pdf(pdf_bytes: bytes) -> List[str]:
    """Extract text from each page of a PDF (returns list of page texts)."""
    texts: List[str] = []
    try:
        images = convert_from_bytes(pdf_bytes)
        for img in images:
            text = pytesseract.image_to_string(img)
            texts.append(text)
    except Exception as e:
        texts.append(f"Error extracting text from PDF: {e}")
    return texts
