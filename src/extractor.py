import re
from typing import List, Optional, Dict

def _find(patterns: List[str], text: str) -> Optional[str]:
    """Search for the first matching pattern in text and return it."""
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)
    return None


def extract_fields(text: str, doc_type: Optional[str]) -> Dict[str, Optional[str]]:
    """Extract key fields from text based on document type."""
    fields: Dict[str, Optional[str]] = {}

    # ---------------- Invoice ----------------
    if doc_type == "invoice":
        fields["invoice_number"] = _find([
            r"INV[0-9]+",
            r"Invoice\s*No[:\s]*[A-Za-z0-9-]+"
        ], text)
        fields["date"] = _find([
            r"\d{2}/\d{2}/\d{4}",
            r"Date[:\s]*\d{4}-\d{2}-\d{2}"
        ], text)
        fields["total_amount"] = _find([
            r"Total[:\s]*\d+\.?\d*",
            r"\$\d+\.?\d*"
        ], text)

    # ---------------- Resume ----------------
    elif doc_type == "resume":
        fields["email"] = _find([
            r"[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,}"
        ], text)
        fields["phone"] = _find([
            r"\+?\d{10,15}"
        ], text)
        fields["name"] = _find([
            r"Name[:\s]*[A-Z][a-z]+\s[A-Z][a-z]+"
        ], text)

    # ---------------- ID Documents ----------------
    elif doc_type == "id_document":
        fields["id_number"] = _find([
            r"[A-Z0-9]{6,12}",   # Passport, Aadhaar, PAN-like IDs
            r"ID[:\s]*[A-Za-z0-9-]+"
        ], text)
        fields["dob"] = _find([
            r"\d{2}/\d{2}/\d{4}",
            r"Date\s*of\s*Birth[:\s]*\d{2}-\d{2}-\d{4}"
        ], text)
        fields["name"] = _find([
            r"[A-Z][a-z]+\s[A-Z][a-z]+"   # Simple Name Match
        ], text)

    # ---------------- Prescriptions ----------------
    elif doc_type == "prescription":
        fields["doctor_name"] = _find([
            r"Dr\.\s*[A-Z][a-z]+"
        ], text)
        fields["patient_name"] = _find([
            r"Patient[:\s]*[A-Z][a-z]+\s[A-Z][a-z]+"
        ], text)
        fields["medication"] = _find([
            r"[A-Za-z]+\s*\d+mg",
            r"Tablet\s*[A-Za-z0-9]+"
        ], text)

    # ---------------- Bank Statements ----------------
    elif doc_type == "bank_statement":
        fields["account_number"] = _find([
            r"Account\s*Number[:\s]*\d+",
            r"\d{9,18}"
        ], text)
        fields["ifsc"] = _find([
            r"[A-Z]{4}0[A-Z0-9]{6}"   # IFSC code format
        ], text)
        fields["transaction_amount"] = _find([
            r"INR\s*\d+\.?\d*",
            r"\$\d+\.?\d*"
        ], text)

    # ---------------- Generic ----------------
    else:
        fields["generic_id"] = _find([
            r"ID[:\s]*[A-Za-z0-9-]+"
        ], text)

    return fields


def assign_confidence(value: Optional[str], text: str) -> float:
    """Assign a simple confidence score based on whether value exists in text."""
    if value and value.lower() in text.lower():
        return 0.95
    elif value:
        return 0.7
    return 0.0
