from pathlib import Path
import os

# 設定檔案路徑
script_dir = Path(__file__).resolve().parent
os.chdir(script_dir) # 確保目錄正確
todo_file = script_dir / "todo.txt"

def load_tasks():
    """讀取 todo.txt 的任務"""
    if not todo_file.exists():
        return[]
    tasks = []
    with open(todo_file, "r", encoding="utf=8") as file:
        for line in file:
            status, task = line.strip().split(" | ")
            tasks.append({"task": task, "done": status == "完成"})
    return tasks

def save_tasks(tasks):
    """儲存到 todo.txt"""
    with open(todo_file, "w", encoding="utf-8") as file:
        for task in tasks:
            status = "完成" if task["done"] else "未完成"
            file.write(f"{status} | {task['task']}\n")

def add_task(task):
    """新增"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"新增任務:{task}")

def list_tasks():
    """列出所有"""
    tasks = load_tasks()
    if not tasks:
        print("沒有待辦！")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['task']}")

def complete_task(index):
    """標記完成"""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"完成: {tasks[index-1]['task']}")
    else:
        print("無效！")

def delete_task(index):
    """刪除"""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        task = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"刪除: {task['task']}")
    else:
        print("無效！")

def main():
    """主程式"""
    print("歡迎使用TodoList！")
    while True:
        print("\n指令: add/list/done/delete/exit")
        cmd = input("輸入指令:").strip().lower()
        if cmd == "exit":
            print("BYE!")
            break
        elif cmd.startswith("add "):
            task = cmd[4:].strip()
            if task:
                add_task(task)
            else:
                print("不能為空白")
        elif cmd == 'list':
            list_tasks()
        elif cmd.startswith("done "):
            try:
                index = int(cmd[5:])
                complete_task(index)
            except ValueError:
                print("請輸入編號！")
        elif cmd.startswith("delete "):
            try:
                index = int(cmd[7:])
                delete_task(index)
            except:
                print("請輸入編號！")
        else:
            print("無效指令！")

if __name__ == "__main__":
    main()

