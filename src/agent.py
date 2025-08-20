import os
from langchain_community.chat_models import ChatOpenAI

from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from schemas import InvoiceSchema

# Load your API key (already set in environment)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 1️⃣ Create parser from Pydantic schema
parser = PydanticOutputParser(pydantic_object=InvoiceSchema)

# 2️⃣ Create prompt
prompt = ChatPromptTemplate.from_template(
    "Extract the invoice fields from this text:\n{text}\n\nOutput in JSON according to the schema."
)

# 3️⃣ Create LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# 4️⃣ Example text (replace with OCR output later)
text = """
Invoice Number: INV-123
Date: 2025-08-20
Vendor: ACME Corp
Total Amount: 120.50
Line Items:
- Widget, Quantity: 2, Price: 50.0
"""

# 5️⃣ Generate structured output
output = llm(prompt.format_prompt(text=text).to_messages())
result = parser.parse(output[0].content)

print(result.model_dump_json(indent=2))
