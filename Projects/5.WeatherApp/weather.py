import requests

API_KEY = "YOUR_API_KEY_HERE"  # Thay bằng API key của bạn
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#London,GB

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric",
        "lang": "vi"  # Ngôn ngữ tiếng Việt
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        print("❌ Không tìm thấy thành phố hoặc có lỗi xảy ra.")
        print("🔍 Chi tiết lỗi:", data.get("message", "Không rõ"))
        return

    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"\n📍 Thời tiết tại {city}, {country}")
    print(f"🌡 Nhiệt độ: {temperature}°C")
    print(f"🌥 Trạng thái: {weather}")
    print(f"💧 Độ ẩm: {humidity}%")
    print(f"🌬 Gió: {wind} m/s")

def main():
    print("🌦 WEATHER APP - OpenWeatherMap")
    city = input("🔎 Nhập tên thành phố: ")
    if city:
        get_weather(city)
    else:
        print("❌ Tên thành phố không được để trống.")

if __name__ == "__main__":
    main()
