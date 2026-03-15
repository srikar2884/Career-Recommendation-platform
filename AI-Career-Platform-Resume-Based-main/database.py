import sqlite3


def init_db():

    conn = sqlite3.connect("career.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS resumes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        path TEXT,
        skills TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_user(username,email,password):

    conn = sqlite3.connect("career.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(username,email,password) VALUES(?,?,?)",
        (username,email,password)
    )

    conn.commit()
    conn.close()


def login_user(email,password):

    conn = sqlite3.connect("career.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email,password)
    )

    user = cur.fetchone()

    conn.close()

    return user


def save_resume(user_id,path,skills):

    conn = sqlite3.connect("career.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO resumes(user_id,path,skills) VALUES(?,?,?)",
        (user_id,path,skills)
    )

    conn.commit()
    conn.close()


def get_last_resume(user_id):

    conn = sqlite3.connect("career.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM resumes WHERE user_id=? ORDER BY id DESC LIMIT 1",
        (user_id,)
    )

    resume = cur.fetchone()

    conn.close()

    return resume