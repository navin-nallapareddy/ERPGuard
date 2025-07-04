from pathlib import Path
from erpguard.database.connection import get_connection

SQL_FILE = Path(__file__).resolve().parents[2] / "docker-entrypoint-initdb.sql"


def initialize_database() -> None:
    """Execute the SQL schema file against the configured database."""
    with SQL_FILE.open() as f:
        sql = f.read()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized")
