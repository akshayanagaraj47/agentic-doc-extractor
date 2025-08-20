from schemas import InvoiceSchema

# Example usage
invoice = InvoiceSchema(
    invoice_number="INV-001",
    date="2025-08-20",
    vendor="ACME Corp",
    total_amount=120.50,
    line_items=[{"description": "Widget", "quantity": 2, "price": 50.0}]
)

# Updated for Pydantic v2
print(invoice.model_dump_json(indent=2))
