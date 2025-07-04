from fpdf import FPDF
from database.connection import get_connection

pdf = FPDF()
pdf.set_font("Arial", size=12)
pdf.add_page()
pdf.cell(200, 10, "ERPGuard Compliance Audit Report", ln=True, align='C')

conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM rule_results WHERE status='FAIL'")
total_fails = cur.fetchone()[0]
if total_fails == 0:
    pdf.cell(200, 10, "RESULT: ✅ FULLY COMPLIANT", ln=True)
else:
    pdf.cell(200, 10, f"RESULT: ❌ NON-COMPLIANT - {total_fails} issues found", ln=True)
pdf.ln(10)
pdf.cell(200, 10, "Detailed Findings:", ln=True)
cur.execute("SELECT table_name, record_key, rule_name, message FROM rule_results WHERE status='FAIL'")
for row in cur.fetchall():
    pdf.cell(200, 8, f"{row[0]}[{row[1]}] - Rule: {row[2]} -> {row[3]}", ln=True)
pdf.output("Compliance_Report.pdf")