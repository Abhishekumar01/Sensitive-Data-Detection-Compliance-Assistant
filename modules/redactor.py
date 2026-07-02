"""Sensitive Data Masking Module"""

import re


def mask_email(email):

    username, domain = email.split("@")

    if len(username) <= 2:
        return "*" * len(username) + "@" + domain

    return (
        username[:2]
        + "*" * (len(username) - 2)
        + "@"
        + domain
    )


def mask_phone(phone):

    digits = re.sub(r"\D", "", phone)

    if len(digits) < 10:
        return phone

    return digits[:2] + "******" + digits[-2:]


def mask_aadhaar(aadhaar):

    digits = re.sub(r"\D", "", aadhaar)

    return digits[:4] + "****" + digits[-4:]


def mask_pan(pan):

    return pan[:2] + "****" + pan[-3:]


def mask_credit_card(card):

    digits = re.sub(r"\D", "", card)

    return "*" * (len(digits) - 4) + digits[-4:]


def mask_bank(account):

    digits = re.sub(r"\D", "", account)

    return "*" * (len(digits) - 4) + digits[-4:]


def mask_password(password):

    return "********"


def mask_api_key(key):

    return "********"


def mask_text(text):

    # Email
    text = re.sub(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        lambda m: mask_email(m.group()),
        text,
    )

    # Phone
    text = re.sub(
        r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b",
        lambda m: mask_phone(m.group()),
        text,
    )

    # Aadhaar
    text = re.sub(
        r"\b\d{4}\s?\d{4}\s?\d{4}\b",
        lambda m: mask_aadhaar(m.group()),
        text,
    )

    # PAN
    text = re.sub(
        r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
        lambda m: mask_pan(m.group()),
        text,
    )

    # Credit Card
    text = re.sub(
        r"\b(?:\d[ -]*?){13,16}\b",
        lambda m: mask_credit_card(m.group()),
        text,
    )

    # Password
    text = re.sub(
        r"(?i)(password|pwd)(\s*[:=]\s*)([^\s]+)",
        lambda m: m.group(1) + m.group(2) + mask_password(m.group(3)),
        text,
    )

    # API Key
    text = re.sub(
        r"(?i)(api[_-]?key|token|secret)(\s*[:=]\s*)([A-Za-z0-9_\-]{10,})",
        lambda m: m.group(1) + m.group(2) + mask_api_key(m.group(3)),
        text,
    )

    # Bank Account
    text = re.sub(
        r"\b\d{9,18}\b",
        lambda m: mask_bank(m.group()),
        text,
    )

    return text