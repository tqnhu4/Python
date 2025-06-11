# 🚀 Flask Basic App

Đây là một ứng dụng web cơ bản sử dụng [Flask](https://flask.palletsprojects.com/) – một micro web framework bằng Python. Ứng dụng minh họa những chức năng nền tảng của một web app như routing, xử lý form và render template HTML.

---

## 📌 Tính năng

- Trang chủ (`/`) hiển thị lời chào.
- Trang giới thiệu (`/about`) mô tả ứng dụng.
- Trang nhập tên (`/form`) cho phép người dùng gửi dữ liệu.
- Trang chào người dùng (`/greet/<username>`) phản hồi tên đã nhập.
- Hiển thị danh sách tất cả người dùng đã nhập tên trong session.

---

## 📁 Cấu trúc thư mục

flask_basic_app/
├── app.py # Ứng dụng Flask chính
├── templates/ # Thư mục chứa các file HTML template
│ ├── base.html
│ ├── index.html
│ ├── about.html
│ ├── form.html
│ └── greet.html
├── requirements.txt # (Tùy chọn) danh sách package cần thiết
├── README.md # Tài liệu hướng dẫn

## Tạo môi trường ảo (tuỳ chọn)
python -m venv venv
source venv/bin/activate    # Trên macOS/Linux
venv\Scripts\activate       # Trên Windows

## Cài đặt package
pip install Flask

Hoặc cài từ requirements.txt:

pip install -r requirements.txt

## Chạy ứng dụng

export FLASK_APP=app.py      # Trên macOS/Linux
set FLASK_APP=app.py         # Trên Windows

flask run


Sau đó truy cập trình duyệt tại: http://127.0.0.1:5000

## Giao diện người dùng
Trang chủ: Hiển thị lời chào đơn giản

Giới thiệu: Mô tả về app

Nhập tên: Người dùng nhập tên vào form

Lời chào: Hiển thị tên người dùng + danh sách tên đã nhập