SELECT * FROM tasks
LIMIT 100;

SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM status;
SELECT COUNT(*) FROM tasks;
SELECT * FROM users LIMIT 5;

SELECT * FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'in progress')
WHERE id = 1;

SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

SELECT u.id, u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id
HAVING task_count = 0;

INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Нова задача', 'Опис завдання', (SELECT id FROM status WHERE name = 'new'), 1);

SELECT * FROM tasks
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

DELETE FROM tasks
WHERE id = 1;

SELECT * FROM users
WHERE email LIKE '%@example.com';

UPDATE users
SET fullname = 'Нове '
WHERE id = 1;

SELECT s.name, COUNT(t.id) AS task_count
FROM status s
LEFT JOIN tasks t ON s.id = t.status_id
GROUP BY s.id;

SELECT t.*
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%@example.com';

SELECT * FROM tasks
WHERE description IS NULL OR TRIM(description) = '';

SELECT u.fullname, t.*
FROM users u
INNER JOIN tasks t ON u.id = t.user_id
WHERE t.status_id = (SELECT id FROM status WHERE name = 'in progress');

SELECT u.fullname, COUNT(t.id) AS task_count
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
GROUP BY u.id;







