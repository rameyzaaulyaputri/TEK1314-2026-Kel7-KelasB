# SEBELUM
query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}';"
conn = get_conn()
cur = conn.cursor()
try:
    cur.execute(query)
    row = cur.fetchone()
