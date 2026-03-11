import sqlite3

DB_NAME = "chat.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_chat(question, answer):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO chat_history (question, answer) VALUES (?, ?)",
        (question, answer)
    )

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM chat_history ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    return [{"question": r[0], "answer": r[1]} for r in rows]