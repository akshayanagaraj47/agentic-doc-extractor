from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from typing import Optional, List
import os
import platform
import shutil


# ---------- Auto detect tesseract path ----------
def setup_tesseract():
    system = platform.system()

    if system == "Windows":
        # Check common Windows install path
        possible_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        if os.path.exists(possible_path):
            pytesseract.pytesseract.tesseract_cmd = possible_path

    else:
        # On Linux (Streamlit Cloud) → rely on PATH
        if shutil.which("tesseract"):
            pytesseract.pytesseract.tesseract_cmd = shutil.which("tesseract")


# Run setup on import
setup_tesseract()


# ---------- OCR Functions ----------
def extract_text_from_image(image: Image.Image) -> Optional[str]:
    """Extract text from a PIL image using Tesseract OCR."""
    try:
        return pytesseract.image_to_string(image)
    except Exception as e:
        return f"[ERROR extracting image text: {e}]"


def extract_text_from_pdf(pdf_bytes: bytes) -> List[str]:
    """Extract text from each page of a PDF (returns list of page texts)."""
    texts: List[str] = []
    try:
        images = convert_from_bytes(pdf_bytes)
        for img in images:
            text = pytesseract.image_to_string(img)
            texts.append(text)
    except Exception as e:
        texts.append(f"[ERROR extracting PDF text: {e}]")
    return texts
