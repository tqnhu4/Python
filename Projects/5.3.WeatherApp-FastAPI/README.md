# 🌤 Weather App - Dự báo thời tiết bằng FastAPI

Đây là một ứng dụng RESTful API đơn giản sử dụng **Python FastAPI** để hiển thị thông tin thời tiết theo tên thành phố, thông qua dữ liệu từ [OpenWeatherMap API](https://openweathermap.org/api).

---

## 🚀 Tính năng

- Lấy thông tin thời tiết hiện tại theo tên thành phố
- Dữ liệu thời tiết bao gồm:
  - Mô tả thời tiết
  - Nhiệt độ hiện tại
  - Cảm giác như
  - Độ ẩm
  - Tốc độ gió
- Swagger UI để kiểm thử API trực quan
- Giao diện API thân thiện, dễ dùng

---

## 🧰 Công nghệ sử dụng

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Requests](https://docs.python-requests.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- Python 3.8+

---

## 📦 Cài đặt

## Environment:
- OPENWEATHER_API_KEY=your_openweathermap_api_key

## Install Library
- pip install -r requirements.txt

## If get error
### Tạo venv mới
- python3 -m venv venv

### Kích hoạt venv
- source venv/bin/activate

### Cài đặt dependencies
- pip install -r requirements.txt


## Run
- uvicorn main:app --reload

## Browser
- Swagger UI: http://localhost:8000/docs

- Redoc: http://localhost:8000/redoc

