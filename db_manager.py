from typing import Generator
import os
from dotenv import load_dotenv
import psycopg

load_dotenv()
password = os.getenv("passwords")

url = f"postgresql://postgres.slcwqkacolixtbssmhdx:{password}@aws-1-us-east-2.pooler.supabase.com:6543/postgres"

def get_db_cursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()