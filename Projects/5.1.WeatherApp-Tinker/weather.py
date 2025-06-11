import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'


def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên thành phố")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=vi"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        result = (
            f"Thời tiết: {weather}\n"
            f"Nhiệt độ: {temp}°C\n"
            f"Cảm giác như: {feels_like}°C\n"
            f"Độ ẩm: {humidity}%\n"
            f"Gió: {wind} m/s"
        )
        result_label.config(text=result)
    except requests.exceptions.HTTPError:
        messagebox.showerror("Lỗi", "Không tìm thấy thành phố")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi lấy dữ liệu: {str(e)}")

# Tạo giao diện
root = tk.Tk()
root.title("Ứng dụng Dự báo Thời tiết")
root.geometry("350x300")
root.resizable(False, False)

# Nhập thành phố
tk.Label(root, text="Nhập tên thành phố:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12), width=30)
city_entry.pack()

# Nút lấy thời tiết
tk.Button(root, text="Xem thời tiết", font=("Arial", 12), command=get_weather).pack(pady=10)

# Hiển thị kết quả
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
