def extract_txt_text(txt_path):
    """Read text from a TXT file."""

    try:
        with open(txt_path, "r", encoding="utf-8") as file:
            return file.read()

    except UnicodeDecodeError:
        with open(txt_path, "r", encoding="latin-1") as file:
            return file.read()

    except Exception as e:
        return f"Error reading TXT: {str(e)}"