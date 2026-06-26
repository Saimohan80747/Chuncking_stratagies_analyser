import pandas as pd
from pypdf import PdfReader
from docx import Document


def extract_text(uploaded_file):
    try:
        filename = uploaded_file.filename.lower()
        file_obj = uploaded_file.file

        # PDF
        if filename.endswith(".pdf"):
            reader = PdfReader(file_obj)

            text = ""

            for page in reader.pages:
                text += page.extract_text() or ""
                text += "\n"

            return text

        # CSV
        elif filename.endswith(".csv"):
            df = pd.read_csv(file_obj)
            return df.to_string(index=False)

        # Excel
        elif filename.endswith((".xlsx", ".xls")):
            sheets = pd.read_excel(
                file_obj,
                sheet_name=None
            )

            text = ""

            for sheet_name, df in sheets.items():
                text += f"\n--- {sheet_name} ---\n"
                text += df.to_string(index=False)
                text += "\n"

            return text

        # DOCX
        elif filename.endswith(".docx"):
            doc = Document(file_obj)

            return "\n".join(
                para.text
                for para in doc.paragraphs
                if para.text.strip()
            )

        # TXT
        elif filename.endswith(".txt"):
            return file_obj.read().decode(
                "utf-8",
                errors="ignore"
            )

        return "Unsupported file type"

    except Exception as e:
        return f"Error extracting text: {str(e)}"