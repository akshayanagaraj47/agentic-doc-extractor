from typing import Optional

def detect_doc_type(text: str) -> Optional[str]:
    """
    Determine document type based on text content.
    Returns one of: invoice, resume, id_document, prescription, bank_statement, generic
    """
    if not text:
        return "generic"

    lowered = text.lower()

    # Invoice / Bills
    if "invoice" in lowered or "bill" in lowered or "total amount" in lowered:
        return "invoice"

    # Resume / CV
    elif "education" in lowered or "experience" in lowered or "resume" in lowered or "curriculum vitae" in lowered:
        return "resume"

    # ID Documents
    elif "id" in lowered or "passport" in lowered or "driver" in lowered or "license" in lowered or "aadhaar" in lowered:
        return "id_document"

    # Medical Prescription
    elif "dr." in lowered or "prescription" in lowered or "take once daily" in lowered or "mg" in lowered:
        return "prescription"

    # Bank Statements
    elif "account number" in lowered or "transaction" in lowered or "ifsc" in lowered or "debit" in lowered:
        return "bank_statement"

    # Default
    else:
        return "generic"
