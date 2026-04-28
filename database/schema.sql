-- database/schema.sql
-- 建立 tasks 資料表

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    is_completed INTEGER NOT NULL DEFAULT 0,
    due_date TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
