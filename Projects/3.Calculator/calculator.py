import tkinter as tk

def click(event):
    global expression
    expression += str(event.widget["text"])
    input_var.set(expression)

def clear():
    global expression
    expression = ""
    input_var.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_var.set(result)
        expression = result  # để tiếp tục tính tiếp
    except:
        input_var.set("Error")
        expression = ""

# Khởi tạo ứng dụng
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")

expression = ""
input_var = tk.StringVar()

# Entry hiển thị biểu thức
entry = tk.Entry(root, textvariable=input_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Tạo các nút
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(row_frame, text=char, font="Arial 18", height=2, width=4)
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        if char == "=":
            btn.config(command=equal)
        else:
            btn.bind("<Button-1>", click)

# Nút Clear
clear_btn = tk.Button(root, text="C", font="Arial 18", bg="red", fg="white", command=clear)
clear_btn.pack(fill="both", expand=True, padx=10, pady=10)

# Chạy ứng dụng
root.mainloop()
