# 📄 Agentic Document Extractor (Regex-Only)

A Streamlit app that ingests PDFs or images, runs OCR, **auto-detects document type** (invoice / bill / prescription / ID / resume / bank statement), extracts key fields with **regex**, assigns **per-field & overall confidence**, does simple **QA checks**, and returns a clean JSON with a **Download** button.

> Built to satisfy the “Agentic Document Extraction Challenge” without paid LLMs (uses OCR + regex). Easy to extend to LLMs later.

---

## ✨ Features
- Upload **PDF** or **Image** (PNG/JPG/JPEG)
- OCR (Tesseract) for scanned docs
- Routing to detect doc type (invoice, prescription, id_document, resume, bank_statement, generic)
- Regex-based field extraction (invoice no., date, amount, name, etc.)
- Confidence score per field + overall average
- Basic QA validations (date/amount shape checks)
- JSON preview + **Download JSON**

---

## 🧱 Tech Stack
- Python 3.9
- Streamlit
- Tesseract OCR (`pytesseract`)
- PyMuPDF and/or pdf2image + PIL
- Regex + light heuristics

---

## 📦 Requirements
- **Python 3.9**
- **Tesseract OCR**
  - Windows typical path: `C:\Program Files\Tesseract-OCR\`
  - Add that folder to your **PATH**
- **For PDFs**
  - If using **pdf2image**: install **Poppler** and add its `bin` folder to **PATH**
  - If using **PyMuPDF (fitz)**: no Poppler needed

> This project works locally with Tesseract installed. No API keys needed.

---

## 🚀 Setup

```bash
# From project root
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
