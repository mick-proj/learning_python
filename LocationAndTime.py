import requests
from datetime import datetime
import pytz

def get_location():
    """Get approximate location based on your public IP."""
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data["city"], data["country"], data["lat"], data["lon"], data["timezone"]
    except:
        return None

def get_sun_times(lat, lon):
    """Get sunrise and sunset times for given coordinates."""
    try:
        url = f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&formatted=0"
        response = requests.get(url)
        data = response.json()["results"]
        return data["sunrise"], data["sunset"]
    except:
        return None, None

if __name__ == "__main__":
    location = get_location()
    if location:
        city, country, lat, lon, tz = location
        sunrise_utc, sunset_utc = get_sun_times(lat, lon)

        # Convert times to local timezone
        local_tz = pytz.timezone(tz)
        sunrise_local = datetime.fromisoformat(sunrise_utc).astimezone(local_tz).strftime("%H:%M")
        sunset_local = datetime.fromisoformat(sunset_utc).astimezone(local_tz).strftime("%H:%M")

        now = datetime.now(local_tz).strftime("%Y-%m-%d %H:%M")

        print(f"📍 Location: {city}, {country}")
        print(f"⏰ Current time: {now}")
        print(f"🌅 Sunrise: {sunrise_local}")
        print(f"🌇 Sunset:  {sunset_local}")
    else:
        print("❌ Could not determine location.")
