import pandas as pd
from pypdf import PdfReader
from docx import Document




def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()

   
    if filename.endswith(".pdf"):
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    
    elif filename.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        return df.to_string(index=False)

    
    elif filename.endswith((".xlsx", ".xls")):
        sheets = pd.read_excel(uploaded_file, sheet_name=None)

        text = ""
        for sheet, df in sheets.items():
            text += f"\n--- {sheet} ---\n"
            text += df.to_string()
            text += "\n"

        return text

   
    elif filename.endswith(".docx"):
        doc = Document(uploaded_file)
        return "\n".join(p.text for p in doc.paragraphs)

    
    elif filename.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    return "Unsupported file type"


