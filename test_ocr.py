from PIL import Image
import pytesseract

# Point to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load an image (replace with your file)
image = Image.open("test.png")  # <-- put a test image in this folder
text = pytesseract.image_to_string(image)

print("OCR Result:")
print(text)
