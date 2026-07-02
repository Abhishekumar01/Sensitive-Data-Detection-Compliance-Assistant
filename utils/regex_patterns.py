"""Centralized Regular Expressions Sensitive Data Compliance Assistant"""

REGEX_PATTERNS = {

    # Email Address

    "Email Address":
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    # Indian Mobile Number

    "Phone Number":
    r"(?<!\d)(?:\+91[- ]?)?[6-9]\d{9}(?!\d)",

    # Aadhaar Number
    # Supports:
    # 123412341234
    # 1234 1234 1234

    "Aadhaar Number":
    r"\b\d{4}(?:\s\d{4}){2}\b|\b\d{12}\b",

    # PAN Number

    "PAN Number":
    r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",

    # Credit Card Supports:
    # 4111111111111111
    # 4111 1111 1111 1111
    # 4111-1111-1111-1111

    "Credit Card":
    r"\b(?:\d{4}[- ]?){3}\d{4}\b|\b\d{13,16}\b",

    # IFSC Code

    "IFSC Code":
    r"\b[A-Z]{4}0[A-Z0-9]{6}\b",

    # Employee ID

    "Employee ID":
    r"(?i)\bEMP\d{3,6}\b",

    # Password

    "Password":
    r"(?i)(?:password|pwd)\s*[:=]\s*['\"]?([^\s,'\"]+)['\"]?",

    # API Key / Token / Secret

    "API Key":
    r"(?i)(?:api[_-]?key|token|secret)\s*[:=]\s*['\"]?([A-Za-z0-9_\-]{10,})['\"]?"
}