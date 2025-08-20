import streamlit as st
from router import detect_doc_type
from ocr_utils import extract_text_from_image, extract_text_from_pdf
from extractor import extract_fields, assign_confidence
from validator import validate_data

st.title("📄 Intelligent Document Extractor")

uploaded_file = st.file_uploader("Upload a PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    # Save temporarily
    if uploaded_file.type == "application/pdf":
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        text = extract_text_from_pdf("temp.pdf")
    else:
        with open("temp.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        text = extract_text_from_image("temp.png")

    # Show extracted text
    st.subheader("📜 Extracted Text")
    st.text(text[:1000])  # show first 1000 characters only

    # Detect document type
    doc_type = detect_doc_type(text)
    st.subheader("📌 Detected Document Type")
    st.write(doc_type)

    # Extract structured fields
    data = extract_fields(text, doc_type)
    st.subheader("🗂 Extracted Data")
    st.json(data)

    # Confidence scores
    scores = {k: assign_confidence(v, text) for k, v in data.items()}
    st.subheader("📊 Confidence Scores")
    st.json(scores)

    # Validate data
    errors = validate_data(data)
    st.subheader("✅ Validation Results")
    if errors:
        st.error(errors)
    else:
        st.success("All fields validated successfully!")
