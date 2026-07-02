"""
Report Generator Module

Creates:
1. TXT Compliance Report
2. PDF Compliance Report
"""

import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

REPORT_FOLDER = "reports"


def ensure_report_folder():
    """Create reports folder if it does not exist."""
    os.makedirs(REPORT_FOLDER, exist_ok=True)


def build_report_text(filename, results, risk):
    """Build report text."""

    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    report = []

    report.append("=" * 65)
    report.append("      Sensitive Data Compliance Report")
    report.append("=" * 65)
    report.append("")

    report.append(f"Generated On : {now}")
    report.append(f"Document     : {filename}")
    report.append(f"Risk Level   : {risk['level']}")
    report.append(f"Risk Score   : {risk['score']}")
    report.append("")

    report.append("-" * 65)
    report.append("Detected Sensitive Information")
    report.append("-" * 65)
    report.append("")

    if results:

        for item in results:

            report.append(f"Category : {item['type']}")
            report.append(f"Count    : {item['count']}")

            report.append("Values:")

            for value in item["values"]:
                report.append(f"   • {value}")

            report.append("")

    else:

        report.append("No sensitive information detected.")
        report.append("")

    report.append("-" * 65)
    report.append("Risk Breakdown")
    report.append("-" * 65)
    report.append("")

    for row in risk["breakdown"]:

        report.append(
            f"{row['Type']} | "
            f"Count: {row['Count']} | "
            f"Weight: {row['Weight']} | "
            f"Score: {row['Score']}"
        )

    report.append("")
    report.append("=" * 65)

    if risk["level"] == "High":

        report.append("Recommendation:")
        report.append("Immediate review required.")
        report.append("Remove sensitive information before sharing.")

    elif risk["level"] == "Medium":

        report.append("Recommendation:")
        report.append("Review and redact confidential information.")

    else:

        report.append("Recommendation:")
        report.append("Low compliance risk.")

    report.append("")
    report.append("=" * 65)

    return "\n".join(report)


def generate_txt_report(filename, results, risk):
    """Generate TXT report."""

    ensure_report_folder()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    txt_path = os.path.join(
        REPORT_FOLDER,
        f"compliance_report_{timestamp}.txt"
    )

    report = build_report_text(filename, results, risk)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(report)

    return txt_path


def generate_pdf_report(filename, results, risk):
    """Generate PDF report."""

    ensure_report_folder()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    pdf_path = os.path.join(
        REPORT_FOLDER,
        f"compliance_report_{timestamp}.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>Sensitive Data Compliance Report</b>", styles["Title"])
    )

    story.append(
        Paragraph(f"<b>Document:</b> {filename}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Risk Level:</b> {risk['level']}", styles["Normal"])
    )

    story.append(
        Paragraph(f"<b>Risk Score:</b> {risk['score']}", styles["Normal"])
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph("<b>Detected Information</b>", styles["Heading2"])
    )

    if results:

        for item in results:

            story.append(
                Paragraph(
                    f"<b>{item['type']}</b> "
                    f"(Count: {item['count']})",
                    styles["Heading3"]
                )
            )

            for value in item["values"]:

                story.append(
                    Paragraph(value, styles["Normal"])
                )

    else:

        story.append(
            Paragraph(
                "No sensitive information detected.",
                styles["Normal"]
            )
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph("<b>Risk Breakdown</b>", styles["Heading2"])
    )

    for row in risk["breakdown"]:

        story.append(
            Paragraph(
                f"{row['Type']} | "
                f"Count: {row['Count']} | "
                f"Weight: {row['Weight']} | "
                f"Score: {row['Score']}",
                styles["Normal"]
            )
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    if risk["level"] == "High":

        recommendation = (
            "<b>Recommendation:</b> "
            "Immediate review required."
        )

    elif risk["level"] == "Medium":

        recommendation = (
            "<b>Recommendation:</b> "
            "Review and redact confidential information."
        )

    else:

        recommendation = (
            "<b>Recommendation:</b> "
            "Low compliance risk."
        )

    story.append(
        Paragraph(recommendation, styles["Heading2"])
    )

    doc.build(story)

    return pdf_path