# hello_world_gui.py
import tkinter as tk

def say_hello():
    label.config(text="Hello, World!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Hello App")

# Nút bấm
button = tk.Button(root, text="Click Me!", command=say_hello)
button.pack(pady=10)

# Label để hiển thị "Hello, World!"
label = tk.Label(root, text="")
label.pack(pady=10)

# Bắt đầu vòng lặp sự kiện GUI
root.mainloop()
