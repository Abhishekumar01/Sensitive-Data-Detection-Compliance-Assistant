"""Sensitive Data Detection Module
--------------------------------
Detects sensitive information using
regular expressions and contextual rules."""

import re
from utils.regex_patterns import REGEX_PATTERNS

# Confidential Business Keywords

CONFIDENTIAL_KEYWORDS = [
    "confidential",
    "internal use only",
    "salary",
    "trade secret",
    "financial report",
    "merger",
    "acquisition",
    "client database",
    "restricted",
    "private"
]

# Context-Based Bank Account Detection

def detect_bank_accounts(text):
    """
    Detect bank account numbers only when
    they appear near banking keywords.
    """

    pattern = (
        r"(?i)"
        r"(?:"
        r"account(?:\s*number)?"
        r"|bank\s*account"
        r"|a/c"
        r"|acct"
        r")"
        r"\s*[:\-]?\s*"
        r"(\d{9,18})"
    )

    return re.findall(pattern, text)


# Helper Function

def remove_duplicates(values):
    """
    Removes duplicates while preserving order.
    """

    return list(dict.fromkeys(values))


# Main Detection Function

def detect_sensitive_data(text):

    detected = []

    phone_numbers = []

    # Regex Detection

    for category, pattern in REGEX_PATTERNS.items():

        matches = re.findall(pattern, text)

        if not matches:
            continue

        # Handle regex groups
        if isinstance(matches[0], tuple):

            extracted = []

            for item in matches:

                value = next(
                    (x for x in item if x),
                    ""
                )

                extracted.append(value)

            matches = extracted

        matches = remove_duplicates(matches)

        if category == "Phone Number":
            phone_numbers = matches.copy()

        detected.append({

            "type": category,

            "count": len(matches),

            "values": matches

        })

    # Context-Based Bank Detection

    bank_accounts = detect_bank_accounts(text)

    if bank_accounts:

        bank_accounts = remove_duplicates(bank_accounts)

        # Remove any numbers already detected
        # as phone numbers

        bank_accounts = [

            number

            for number in bank_accounts

            if number not in phone_numbers

        ]

        if bank_accounts:

            detected.append({

                "type": "Bank Account",

                "count": len(bank_accounts),

                "values": bank_accounts

            })

    # Confidential Keyword Detection

    lower_text = text.lower()

    keyword_hits = []

    for keyword in CONFIDENTIAL_KEYWORDS:

        if keyword in lower_text:

            keyword_hits.append(keyword)

    keyword_hits = remove_duplicates(keyword_hits)

    if keyword_hits:

        detected.append({

            "type": "Confidential Business Information",

            "count": len(keyword_hits),

            "values": keyword_hits

        })

    # Sort by Count

    detected.sort(

        key=lambda item: item["count"],

        reverse=True

    )

    return detected