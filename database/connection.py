import os
import psycopg2

def get_connection():
    url = os.getenv('DATABASE_URL')
    if url is None:
        raise Exception("DATABASE_URL is not set!")
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://")
    return psycopg2.connect(url + "?sslmode=require")