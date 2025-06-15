# database.py
import sqlite3

DATABASE_NAME = 'blog.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row # Allows accessing columns by name
    return conn

def init_db():
    conn = get_db_connection()
    # Create posts table if it doesn't exist
    conn.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print(f"[*] Database '{DATABASE_NAME}' initialized.")

def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
    conn.close()
    return posts

def get_post_by_id(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post

def create_post(title, content, created_at):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content, created_at) VALUES (?, ?, ?)',
                 (title, content, created_at))
    conn.commit()
    conn.close()

def update_post(post_id, title, content):
    conn = get_db_connection()
    conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                 (title, content, post_id))
    conn.commit()
    conn.close()

def delete_post(post_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()