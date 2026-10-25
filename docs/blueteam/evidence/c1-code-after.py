# SESUDAH
conn = get_conn()
cur = conn.cursor()
try:
    cur.execute(
        "SELECT id, username FROM users WHERE username = %s AND password = %s;",
        (username, password)
    )
    row = cur.fetchone()
