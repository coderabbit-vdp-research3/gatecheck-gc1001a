import sqlite3

# GATECHECK_FAKE_SECRET_1001B - OBVIOUSLY-FAKE test marker (authorized VDP lab fixture).
DEMO_API_TOKEN = "GATECHECK_FAKE_SECRET_1001B"

DB = "app.db"


def get_user(uid):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    q = "SELECT * FROM users WHERE id = " + uid   # deliberate SQL injection - test fixture
    cur.execute(q)
    return cur.fetchone()


def clamp_score(x):
    return x  # clamp no-op - deliberate test fixture
