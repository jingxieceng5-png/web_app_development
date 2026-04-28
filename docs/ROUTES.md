# 路由設計文件 (Routes) - 任務管理系統

## 1. 路由總覽表格

本專案採用單一入口的簡單設計，主要操作皆圍繞在任務清單的增刪改查。因為採用 HTML 表單送出，更新與刪除操作會使用 POST 方法。

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
|------|-----------|----------|----------|------|
| 任務列表 | GET | `/` | `index.html` | 顯示所有任務清單，並包含新增任務的表單 |
| 建立任務 | POST | `/tasks/add` | — | 接收表單資料，存入 DB，完成後重導向至 `/` |
| 編輯任務頁面 | GET | `/tasks/<id>/edit` | `edit.html` | 顯示特定任務的編輯表單 |
| 更新任務 | POST | `/tasks/<id>/update` | — | 接收編輯表單資料，更新 DB，完成後重導向至 `/` |
| 刪除任務 | POST | `/tasks/<id>/delete` | — | 從 DB 中刪除該任務，完成後重導向至 `/` |
| 切換完成狀態 | POST | `/tasks/<id>/toggle_status`| — | 切換任務的完成狀態，完成後重導向至 `/` |

## 2. 每個路由的詳細說明

### 任務列表 (GET `/`)
- **輸入**：無
- **處理邏輯**：呼叫 `TaskModel.get_all()` 取得所有任務資料。
- **輸出**：渲染 `index.html`，並將任務列表傳入模板中顯示。
- **錯誤處理**：無特殊錯誤，若尚未有資料則傳送空陣列。

### 建立任務 (POST `/tasks/add`)
- **輸入**：HTML 表單欄位 `title` (必填), `description`, `due_date`。
- **處理邏輯**：驗證 `title` 是否存在且不為空字串，通過後呼叫 `TaskModel.create(...)` 寫入資料庫。
- **輸出**：HTTP 302 重導向回首頁 `/`。
- **錯誤處理**：若 `title` 缺失，可拋出 400 Bad Request 或稍後實作 flash 訊息提示使用者。

### 編輯任務頁面 (GET `/tasks/<id>/edit`)
- **輸入**：URL 動態參數 `id`。
- **處理邏輯**：呼叫 `TaskModel.get_by_id(id)` 取出該任務的現有資料。
- **輸出**：渲染 `edit.html`，並將該任務的資料作為預設值填入表單中。
- **錯誤處理**：若資料庫中找不到該 `id`，回傳 404 Not Found。

### 更新任務 (POST `/tasks/<id>/update`)
- **輸入**：URL 動態參數 `id`，表單欄位 `title` (必填), `description`, `due_date`。
- **處理邏輯**：呼叫 `TaskModel.update(...)` 修改資料庫內對應的紀錄。
- **輸出**：HTTP 302 重導向回首頁 `/`。
- **錯誤處理**：若 `title` 缺失回傳 400，若 `id` 不存在則略過或回傳 404。

### 刪除任務 (POST `/tasks/<id>/delete`)
- **輸入**：URL 動態參數 `id`。
- **處理邏輯**：呼叫 `TaskModel.delete(id)` 從資料庫刪除紀錄。
- **輸出**：HTTP 302 重導向回首頁 `/`。
- **錯誤處理**：若 `id` 不存在，可忽略或回傳 404。

### 切換狀態 (POST `/tasks/<id>/toggle_status`)
- **輸入**：URL 動態參數 `id`。
- **處理邏輯**：呼叫 `TaskModel.toggle_status(id)` 進行完成/未完成狀態切換。
- **輸出**：HTTP 302 重導向回首頁 `/`。
- **錯誤處理**：若 `id` 不存在回傳 404。

## 3. Jinja2 模板清單

預計在 `app/templates/` 目錄下建立以下 HTML 檔案：

- **`base.html`**：全站共用版面，包含基本的 `<html>` 結構、`<head>`（引入 CSS/JS 等）與共用的 Header/Footer。
- **`index.html`**：任務列表頁面。繼承自 `base.html`，包含顯示所有任務的迴圈結構，以及最上方的新增任務表單。
- **`edit.html`**：編輯任務頁面。繼承自 `base.html`，提供一個獨立頁面讓使用者能修改現有任務的詳細內容。

## 4. 路由骨架程式碼

已在 `app/routes/task_routes.py` 中建立 Flask Blueprint，並包含了所有路由的函式定義與 Docstring。未來只需填入實作邏輯並引入 `TaskModel` 即可完成開發。
