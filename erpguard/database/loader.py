import pandas as pd
from psycopg2.extras import execute_batch

from .connection import get_connection


def load_dataframe(df: pd.DataFrame, table_name: str) -> None:
    """Replace table contents with DataFrame values."""
    if df.empty:
        return

    columns = list(df.columns)
    records = [tuple(row) for row in df.itertuples(index=False, name=None)]

    placeholders = ", ".join(["%s"] * len(columns))
    cols = ", ".join(columns)
    query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"TRUNCATE {table_name} RESTART IDENTITY")
            execute_batch(cur, query, records)
        conn.commit()
