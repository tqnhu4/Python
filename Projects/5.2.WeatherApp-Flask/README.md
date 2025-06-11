# 🌦 Weather App - Ứng dụng Dự báo Thời tiết với Python Flask

Đây là một ứng dụng web đơn giản sử dụng **Python Flask** để lấy và hiển thị thông tin thời tiết theo thành phố, thông qua API từ [OpenWeatherMap](https://openweathermap.org/).

---

## 📌 Tính năng

- Giao diện người dùng đơn giản, thân thiện
- Hiển thị các thông tin thời tiết:
  - Mô tả thời tiết
  - Nhiệt độ
  - Cảm giác như
  - Độ ẩm
  - Tốc độ gió
- Hỗ trợ ngôn ngữ tiếng Việt
- Xử lý lỗi khi người dùng nhập sai tên thành phố

---

## 🧰 Công nghệ sử dụng

- Python 3.x
- Flask
- Requests
- HTML (Jinja2 Template)

---

## 🚀 Cài đặt và chạy

### Cài đặt các thư viện cần thiết
- pip install flask requests

### Dùng Virtual Environment
### Tạo virtual environment
- python3 -m venv venv

### Kích hoạt virtual environment
- source venv/bin/activate
### Cài đặt gói
- pip install flask requests


## Lấy API key từ OpenWeatherMap
- Đăng ký miễn phí tại https://openweathermap.org/api

- Copy API key và thay vào trong file app.py dòng sau:
-- API_KEY = "your_openweathermap_api_key"

## Chạy ứng dụng:

- python app.py

- Truy cập trình duyệt tại địa chỉ: http://127.0.0.1:5000

## Cấu trúc thư mục

- weather_app/
- ├── app.py
- └── templates/
-     └── index.html
