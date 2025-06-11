from fastapi import FastAPI, Query, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load API_KEY từ .env nếu cần

app = FastAPI(title="Weather App with FastAPI")

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Hoặc thay bằng chuỗi cứng nếu cần

@app.get("/")
def root():
    return {"message": "Welcome to Weather API - use /weather?city=Hanoi"}

@app.get("/weather")
def get_weather(city: str = Query(..., description="City name")):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="API Key not found")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=vi"
    
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found or API error")

    data = response.json()

    return {
        "city": data["name"],
        "weather": data["weather"][0]["description"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
