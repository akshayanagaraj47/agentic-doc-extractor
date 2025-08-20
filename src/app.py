import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import json
import io
from typing import Optional

# Import your helper modules
from ocr_utils import extract_text_from_image, extract_text_from_pdf
from router import detect_doc_type
from extractor import extract_fields, assign_confidence

# Streamlit Page Config
st.set_page_config(page_title="📄 Document Extractor", layout="wide")

st.title("📄 Document Extractor")

# File uploader
uploaded_file: Optional[st.runtime.uploaded_file_manager.UploadedFile] = st.file_uploader(
    "Upload a PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    text_content = ""

    try:
        # Handle PDF
        if uploaded_file.type == "application/pdf":
            st.info("Processing PDF...")
            images = convert_from_bytes(uploaded_file.read())
            for i, img in enumerate(images):
                st.image(img, caption=f"Page {i+1}", use_container_width=True)
                text_content += pytesseract.image_to_string(img) + "\n"

        # Handle Image
        else:
            st.info("Processing Image...")
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            text_content = pytesseract.image_to_string(image)

    except Exception as e:
        st.error(f"❌ Error while processing file: {e}")
        st.stop()

    # Show extracted text
    st.subheader("📝 Extracted Text")
    if text_content.strip():
        st.text_area("Raw Text", text_content, height=200)
    else:
        st.warning("⚠️ No text extracted. Please check file quality or OCR settings.")

    # -------- JSON Integration --------
    doc_type: Optional[str] = detect_doc_type(text_content)
    fields = extract_fields(text_content, doc_type)

    # Assign confidence scores
    fields_with_confidence = {
        field_name: {
            "value": field_value,
            "confidence": assign_confidence(field_value, text_content)
        }
        for field_name, field_value in fields.items()
    }

    # Final JSON result
    result = {
        "document_type": doc_type,
        "extracted_text": text_content.strip(),
        "fields": fields_with_confidence
    }

    # Show JSON output
    st.subheader("📊 JSON Output")
    st.json(result)

    # -------- Download Option --------
    json_bytes = io.BytesIO(json.dumps(result, indent=4).encode("utf-8"))
    st.download_button(
        label="⬇️ Download JSON",
        data=json_bytes,
        file_name="extracted_data.json",
        mime="application/json"
    )
