# Import necessary libraries
import requests             # To send HTTP requests to the weather API
import tkinter as tk        # For building the GUI
from tkinter import messagebox  # For showing popup messages (warnings/errors)

# ------------------ GUI Setup ------------------
window = tk.Tk()                                     # Create the main window
window.title("Weather App By Harsh Saini")           # Window title
window.geometry("700x580")                           # Set window size
window.config(bg="#1e1e2f")                          # Background color

# App title label
title_label = tk.Label(window, text="Weather App", font=("Segoe UI", 20, "bold"),
                       bg="#1e1e2f", fg="#f0f0f5")
title_label.pack(pady=15)

# Input field for city name
city_entry = tk.Entry(window, width=25, font=("Segoe UI", 14),
                      bg="#32334d", fg="#f0f0f5", insertbackground="#f0f0f5",
                      relief="flat")
city_entry.pack(pady=10)


# ------------------ Weather Function ------------------
def get_weather():
    """
    Fetch weather details of the entered city using OpenWeatherMap API.
    """
    city = city_entry.get().strip()  # Get user input (city name)
    if not city:  # Check if input is empty
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    # OpenWeatherMap API key and URL
    api_key = "01ea9720728e89aaaf6e4e076de70916"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)     # Send request to API
        data = response.json()           # Convert response to JSON format

        # If city is found and API response is OK (cod=200)
        if data.get("cod") == 200:
            city_name = data.get("name", "N/A")                      # Extract city name
            country = data.get("sys", {}).get("country", "N/A")      # Extract country code
            temp = data.get("main", {}).get("temp", "N/A")           # Extract temperature
            weather_desc = data.get("weather", [{}])[0].get("description", "N/A").capitalize()

            # Format the result for display
            result = (
                f"City: {city_name}, {country}\n"
                f"Temperature: {temp}°C\n"
                f"Condition: {weather_desc}"
            )
            result_label.config(text=result, fg="#a0e1e0")  # Show result in label
        else:
            # Show error if city not found or API issue
            messagebox.showerror("Error", f"API Error: {data.get('message', 'Unknown error')}")
    except Exception as e:
        # Handle any exceptions (e.g., no internet)
        messagebox.showerror("Error", f"Failed to get data: {e}")


# ------------------ Button & Result Display ------------------
# Button to fetch weather
get_btn = tk.Button(window, text="Get Weather", command=get_weather,
                    font=("Segoe UI", 14), bg="#3a3c5a", fg="#f0f0f5",
                    relief="flat", activebackground="#505273")
get_btn.pack(pady=10)

# Label to display result
result_label = tk.Label(window, text="", font=("Segoe UI", 14),
                        bg="#1e1e2f", fg="#a0e1e0", justify="center")
result_label.pack(pady=20)

# ------------------ Run the App ------------------
window.mainloop()   # Start the GUI event loop
