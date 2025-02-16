from src.api import get_weather
from src.utils import save_to_history

def main():
    print("🌦️ Welcome to the Weather App 🌦️")  # Debugging: Check if the program starts

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == "exit":
            print("Goodbye! 👋")
            break

        weather = get_weather(city)

        if "error" in weather:
            print(f"⚠️ Error: {weather['error']}")
        else:
            print(f"\n🌍 Weather in {city.capitalize()}:")
            print(f"🌡️ Temperature: {weather['temperature']}°C")
            print(f"💧 Humidity: {weather['humidity']}%")
            print(f"🌬️ Wind Speed: {weather['wind_speed']} m/s")
            print(f"☁️ Description: {weather['description']}")

            # Convert weather data to a readable format
            weather_summary = (f"Temperature: {weather['temperature']}°C, "
                               f"Humidity: {weather['humidity']}%, "
                               f"Wind Speed: {weather['wind_speed']} m/s, "
                               f"Description: {weather['description']}")

            # Save history
            save_to_history(city, weather_summary)

if __name__ == "__main__":
    main()
