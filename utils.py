from PyPDF2 import PdfReader

def load_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF file.
    """
    pdf = PdfReader(uploaded_file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text
