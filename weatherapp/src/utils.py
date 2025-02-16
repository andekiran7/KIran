import os

# Ensure the data directory exists
if not os.path.exists("data"):
    os.makedirs("data")

def save_to_history(city, weather):
    """Saves weather data to history.txt"""
    with open("data/history.txt", "a") as file:
        file.write(f"{city}: {weather}\n")

print("✅ utils.py loaded successfully!")  # Debugging
