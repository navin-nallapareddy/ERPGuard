from collections import defaultdict

from erpguard.database.connection import get_connection


def generate_summary() -> dict:
    """Return a summary of rule results grouped by rule name."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """SELECT rule_name, status, COUNT(*) FROM rule_results GROUP BY rule_name, status"""
            )
            summary = defaultdict(dict)
            for rule_name, status, count in cur.fetchall():
                summary[rule_name][status] = count
        return summary


def main() -> None:
    summary = generate_summary()
    for rule, data in summary.items():
        passes = data.get("PASS", 0)
        fails = data.get("FAIL", 0)
        print(f"{rule}: {passes} pass, {fails} fail")


if __name__ == "__main__":
    main()
