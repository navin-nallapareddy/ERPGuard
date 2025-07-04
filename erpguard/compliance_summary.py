
from database.connection import get_connection
conn = get_connection()
cur = conn.cursor()
def generate_summary():
    cur.execute("SELECT COUNT(*) FROM rule_results WHERE status='FAIL'")
    total_fails = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM rule_results WHERE status='FAIL' AND rule_name IN ('must_be_true', 'date_in_future', 'not_expired', 'must_exist_in')")
    critical_fails = cur.fetchone()[0]
    print("=== COMPLIANCE SUMMARY ===")
    if critical_fails > 0:
        print(f"❌ NON-COMPLIANT: {critical_fails} critical issues detected.")
    elif total_fails > 0:
        print(f"⚠ PARTIALLY COMPLIANT: {total_fails} advisory issues detected.")
    else:
        print("✅ FULLY COMPLIANT for configured rules.")
if __name__ == "__main__":
    generate_summary()
