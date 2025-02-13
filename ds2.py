
import sqlite3

conn = sqlite3.connect('tasks.db')  # Це створить файл бази даних, якщо його ще немає
conn.close()  # Закриваємо з'єднання

conn = sqlite3.connect('tasks.db')  
cursor = conn.cursor()

# Створення таблиці користувачів
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
""")

# Створення таблиці статусів
cursor.execute("""
CREATE TABLE IF NOT EXISTS status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);
""")

# Створення таблиці завдань
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES status(id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
""")

conn.commit()
conn.close()
