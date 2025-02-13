import sqlite3
from faker import Faker
import random

# Ініціалізація Faker
fake = Faker()

# Підключення до бази даних (створення файлу tasks.db, якщо його ще немає)
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Створення таблиць (якщо вони не існують)
cursor.executescript("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

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

# Заповнення таблиці status стандартними значеннями
statuses = ['new', 'in progress', 'completed']
for s in statuses:
    try:
        cursor.execute("INSERT INTO status (name) VALUES (?)", (s,))
    except sqlite3.IntegrityError:
        # Якщо запис вже існує, пропустити
        pass

# Заповнення таблиці users випадковими даними
num_users = 10  # кількість користувачів для генерації
for _ in range(num_users):
    fullname = fake.name()
    email = fake.unique.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (?, ?)", (fullname, email))

# Отримання списку id користувачів та статусів
cursor.execute("SELECT id FROM users")
user_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM status")
status_ids = [row[0] for row in cursor.fetchall()]

# Заповнення таблиці tasks випадковими завданнями
num_tasks = 50  # кількість завдань для генерації
for _ in range(num_tasks):
    title = fake.sentence(nb_words=5)
    description = fake.text(max_nb_chars=200)
    user_id = random.choice(user_ids)
    status_id = random.choice(status_ids)
    cursor.execute(
        "INSERT INTO tasks (title, description, status_id, user_id) VALUES (?, ?, ?, ?)",
        (title, description, status_id, user_id)
    )

conn.commit()
conn.close()
