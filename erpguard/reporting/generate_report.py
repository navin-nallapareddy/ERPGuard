from fpdf import FPDF

from erpguard.compliance_summary import generate_summary


OUTPUT_FILE = "compliance_report.pdf"


def create_report(path: str = OUTPUT_FILE) -> None:
    summary = generate_summary()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Compliance Summary", ln=True)
    for rule, data in summary.items():
        passes = data.get("PASS", 0)
        fails = data.get("FAIL", 0)
        pdf.cell(0, 10, f"{rule}: {passes} pass, {fails} fail", ln=True)
    pdf.output(path)


if __name__ == "__main__":
    create_report()
