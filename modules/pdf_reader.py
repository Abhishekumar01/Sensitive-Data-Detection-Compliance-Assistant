import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    """
    Extract text from a PDF document.

    Args:
        pdf_path (str): Path to the uploaded PDF.

    Returns:
        str: Extracted text.
    """

    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        text = f"Error reading PDF: {str(e)}"

    return text