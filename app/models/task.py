import sqlite3
import os

# 預設資料庫路徑：專案根目錄下的 instance/database.db
# __file__ 是 task.py，所以往上三層是專案根目錄 (web_app_development)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
DB_PATH = os.path.join(INSTANCE_DIR, 'database.db')

# 確保 instance 目錄存在
os.makedirs(INSTANCE_DIR, exist_ok=True)

class TaskModel:
    @staticmethod
    def _get_connection():
        """建立並回傳 SQLite 資料庫連線，並設定 row_factory 方便以字典方式存取"""
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def get_all():
        """取得所有任務，依建立時間反序排列 (最新的在最前面)"""
        conn = TaskModel._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @staticmethod
    def get_by_id(task_id):
        """根據 ID 取得單一任務"""
        conn = TaskModel._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @staticmethod
    def create(title, description=None, due_date=None):
        """新增一筆任務"""
        conn = TaskModel._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (title, description, due_date)
            VALUES (?, ?, ?)
        """, (title, description, due_date))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    @staticmethod
    def update(task_id, title, description=None, due_date=None):
        """更新現有任務的內容"""
        conn = TaskModel._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET title = ?, description = ?, due_date = ?
            WHERE id = ?
        """, (title, description, due_date, task_id))
        conn.commit()
        conn.close()

    @staticmethod
    def toggle_status(task_id):
        """切換任務的完成狀態 (完成 <-> 未完成)"""
        task = TaskModel.get_by_id(task_id)
        if not task:
            return False
            
        new_status = 0 if task['is_completed'] else 1
        conn = TaskModel._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks
            SET is_completed = ?
            WHERE id = ?
        """, (new_status, task_id))
        conn.commit()
        conn.close()
        return True

    @staticmethod
    def delete(task_id):
        """刪除特定任務"""
        conn = TaskModel._get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
