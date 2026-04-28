from flask import Blueprint, render_template, request, redirect, url_for, abort

# 建立名為 'task' 的 Blueprint，以便於後續掛載到主程式 app.py 中
task_bp = Blueprint('task', __name__)

@task_bp.route('/')
def index():
    """
    任務列表頁面 (GET /)
    - 呼叫 TaskModel 取得所有任務
    - 渲染 index.html，並將任務資料傳入
    """
    pass

@task_bp.route('/tasks/add', methods=['POST'])
def add_task():
    """
    新增任務 (POST /tasks/add)
    - 接收表單資料 (title, description, due_date)
    - 驗證必填欄位
    - 呼叫 TaskModel.create
    - 成功後重導向至 index
    """
    pass

@task_bp.route('/tasks/<int:task_id>/edit', methods=['GET'])
def edit_task(task_id):
    """
    編輯任務頁面 (GET /tasks/<task_id>/edit)
    - 根據 task_id 呼叫 TaskModel 取得單筆任務資料
    - 若找不到則回傳 404 (使用 abort(404))
    - 渲染 edit.html，並將任務資料傳入
    """
    pass

@task_bp.route('/tasks/<int:task_id>/update', methods=['POST'])
def update_task(task_id):
    """
    更新任務 (POST /tasks/<task_id>/update)
    - 接收表單資料 (title, description, due_date)
    - 呼叫 TaskModel.update
    - 成功後重導向至 index
    """
    pass

@task_bp.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    """
    刪除任務 (POST /tasks/<task_id>/delete)
    - 呼叫 TaskModel.delete
    - 成功後重導向至 index
    """
    pass

@task_bp.route('/tasks/<int:task_id>/toggle_status', methods=['POST'])
def toggle_status(task_id):
    """
    切換任務狀態 (POST /tasks/<task_id>/toggle_status)
    - 呼叫 TaskModel.toggle_status (將未完成設為完成，反之亦然)
    - 成功後重導向至 index
    """
    pass
