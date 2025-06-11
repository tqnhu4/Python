import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("✔ Danh sách rỗng.")
        return
    print("📋 Danh sách công việc:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(tasks):
    task = input("🔹 Nhập công việc mới: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Đã thêm công việc.")
    else:
        print("❌ Công việc không được để trống.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("🔻 Nhập số thứ tự công việc muốn xoá: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"🗑 Đã xoá: {removed}")
        else:
            print("❌ Số thứ tự không hợp lệ.")
    except ValueError:
        print("❌ Nhập vào một số.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO DO LIST ---")
        print("1. Xem danh sách")
        print("2. Thêm công việc")
        print("3. Xoá công việc")
        print("4. Thoát")
        choice = input("👉 Nhập lựa chọn (1-4): ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
