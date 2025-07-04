from collections import defaultdict
import pandas as pd

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


def generate_summary_by_category() -> pd.DataFrame:
    """Return a DataFrame summarizing rule results with derived categories."""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """SELECT rule_name, status, COUNT(*) FROM rule_results GROUP BY rule_name, status"""
            )
            rows = cur.fetchall()

    counts = defaultdict(lambda: {"PASS": 0, "FAIL": 0})
    for rule_name, status, count in rows:
        counts[rule_name][status] = count

    data = []
    for rule_name, results in counts.items():
        category = rule_name.split("_")[0]
        data.append(
            {
                "rule_name": rule_name,
                "category": category,
                "PASS": results.get("PASS", 0),
                "FAIL": results.get("FAIL", 0),
            }
        )

    return pd.DataFrame(data)


def main() -> None:
    summary = generate_summary()
    for rule, data in summary.items():
        passes = data.get("PASS", 0)
        fails = data.get("FAIL", 0)
        print(f"{rule}: {passes} pass, {fails} fail")


if __name__ == "__main__":
    main()
