from pydantic import BaseModel, Field
from typing import List, Optional

# Example schema for an invoice
class LineItem(BaseModel):
    description: str
    quantity: float
    price: float

class InvoiceSchema(BaseModel):
    invoice_number: str = Field(..., description="Invoice number")
    date: str = Field(..., description="Invoice date")
    vendor: str = Field(..., description="Vendor name")
    total_amount: float = Field(..., description="Total invoice amount")
    line_items: Optional[List[LineItem]] = Field([], description="List of line items")
