import os
import psycopg2
from psycopg2.extensions import connection as _Connection


def get_connection() -> _Connection:
    """Create a database connection using the DATABASE_URL env variable."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL environment variable not set")

    # Render databases require SSL. If the connection string does not already
    # specify an sslmode, default to "require" so the same code works locally and
    # in production.
    return psycopg2.connect(database_url, sslmode=os.getenv("PGSSLMODE", "require"))
