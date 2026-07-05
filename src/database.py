import sqlite3
from pathlib import Path

DB_PATH = Path("data/posts.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        generated_at TEXT,
        topic TEXT,
        title TEXT,
        hook TEXT,
        body TEXT,
        cta TEXT,
        hashtags TEXT,
        image_prompt TEXT,
        estimated_read_time INTEGER,
        difficulty TEXT,
        category TEXT,
        model TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_post(post, topic, model):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO posts (
        generated_at,
        topic,
        title,
        hook,
        body,
        cta,
        hashtags,
        image_prompt,
        estimated_read_time,
        difficulty,
        category,
        model
    )
    VALUES (
        datetime('now'),
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
    )
    """, (
        topic,
        post["title"],
        post["hook"],
        post["body"],
        post["cta"],
        ",".join(post["hashtags"]),
        post["image_prompt"],
        post["estimated_read_time"],
        post["difficulty"],
        post["category"],
        model
    ))

    conn.commit()
    conn.close()