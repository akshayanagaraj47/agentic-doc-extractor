from pathlib import Path
from PIL import Image
import pytesseract

# --- Tesseract path ---
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- Paths ---
HERE = Path(__file__).resolve().parent        # src/
DATA_DIR = HERE.parent / "data"               # project/data/
IMG_PATH = DATA_DIR / "test.png"              # project/data/test.png

print("Looking inside:", DATA_DIR)
for f in DATA_DIR.iterdir():
    print(" -", f.name)

print("\nUsing image path:", IMG_PATH)

if not IMG_PATH.exists():
    raise FileNotFoundError(f"❌ Image not found at: {IMG_PATH}")

# --- Open image ---
img = Image.open(IMG_PATH)

# --- OCR ---
text = pytesseract.image_to_string(img, lang="eng")

print("\nOCR Result:\n")
print(text)

# --- Save result ---
OUTPUTS = HERE.parent / "outputs"
OUTPUTS.mkdir(exist_ok=True)
(OUTPUTS / "ocr_result.txt").write_text(text, encoding="utf-8")
print(f"\n✅ Saved OCR text to: {OUTPUTS / 'ocr_result.txt'}")
