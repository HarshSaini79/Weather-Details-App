import requests
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Weather App By Harsh Saini")
window.geometry("700x580")
window.config(bg="#1e1e2f")

title_label = tk.Label(window, text="Weather App", font=("Segoe UI", 20, "bold"), bg="#1e1e2f", fg="#f0f0f5")
title_label.pack(pady=15)

city_entry = tk.Entry(window, width=25, font=("Segoe UI", 14), bg="#32334d", fg="#f0f0f5", insertbackground="#f0f0f5", relief="flat")
city_entry.pack(pady=10)

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    api_key = "01ea9720728e89aaaf6e4e076de70916"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            city_name = data.get("name", "N/A")
            country = data.get("sys", {}).get("country", "N/A")
            temp = data.get("main", {}).get("temp", "N/A")
            weather_desc = data.get("weather", [{}])[0].get("description", "N/A").capitalize()

            result = (
                f"City: {city_name}, {country}\n"
                f"Temperature: {temp}°C\n"
                f"Condition: {weather_desc}"
            )
            result_label.config(text=result, fg="#a0e1e0")
        else:
            messagebox.showerror("Error", f"API Error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to get data: {e}")

get_btn = tk.Button(window, text="Get Weather", command=get_weather, font=("Segoe UI", 14), bg="#3a3c5a", fg="#f0f0f5", relief="flat", activebackground="#505273")
get_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Segoe UI", 14), bg="#1e1e2f", fg="#a0e1e0", justify="center")
result_label.pack(pady=20)

window.mainloop() ye raha uska code