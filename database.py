# database.py
from sqlalchemy import create_engine
from sqlalchemy.sql import text

DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"
engine = create_engine(DATABASE_URL)
conn = engine.connect()

def set_user_role(user):
    set_query = text(f"SET ROLE {user}")
    conn.execute(set_query)

def get_profiles():
    query = text("SELECT * FROM profiles")
    result = conn.execute(query).fetchall()
    return [dict(row._mapping) for row in result]
