import json
from pathlib import Path

from erpguard.database.connection import get_connection


RULES_FILE = Path(__file__).parent / "rules" / "full_compliance_rules.json"


def run_rules() -> None:
    """Execute compliance rules defined in the JSON file."""
    with RULES_FILE.open() as f:
        rules = json.load(f)

    with get_connection() as conn:
        with conn.cursor() as cur:
            for rule in rules:
                name = rule["name"]
                sql = rule["sql"]
                message = rule.get("message", "")

                cur.execute(sql)
                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        record_key = row[0]
                        cur.execute(
                            """
                            INSERT INTO rule_results (table_name, record_key, rule_name, status, message)
                            VALUES (%s, %s, %s, %s, %s)
                            """,
                            ("", record_key, name, "FAIL", message),
                        )
                else:
                    cur.execute(
                        """
                        INSERT INTO rule_results (table_name, record_key, rule_name, status, message)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                        ("", "", name, "PASS", ""),
                    )

            conn.commit()


if __name__ == "__main__":
    run_rules()
