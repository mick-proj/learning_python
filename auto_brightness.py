#!/opt/homebrew/bin/python3
from datetime import datetime, timedelta
from astral import LocationInfo
from astral.sun import sun
import subprocess
import time

# Config
CITY = LocationInfo("Berlin", "Germany")
DAY_LEVEL = 60
NIGHT_LEVEL = 10
FADE_DURATION_MIN = 15
FADE_STEPS = 15

def set_brightness(level: int):
    subprocess.run([
        "/opt/homebrew/bin/m1ddc", "display", "1", "set", "luminance", str(level)
    ])

def fade_brightness(start: int, end: int, duration_minutes: int = FADE_DURATION_MIN):
    steps = FADE_STEPS
    delay = (duration_minutes * 60) / steps
    for i in range(steps + 1):
        level = start + (end - start) * i // steps
        set_brightness(level)
        time.sleep(delay)

while True:
    today = datetime.now()
    s = sun(CITY.observer, date=today)
    sunrise = s["sunrise"].replace(tzinfo=None)
    sunset = s["sunset"].replace(tzinfo=None)
    now = datetime.now()

    if sunrise < now < sunset:
        # It's day now
        set_brightness(DAY_LEVEL)
        # Sleep until sunset, then fade
        sleep_time = (sunset - now).total_seconds()
        time.sleep(max(60, sleep_time))
        fade_brightness(DAY_LEVEL, NIGHT_LEVEL)

    else:
        # It's night now
        set_brightness(NIGHT_LEVEL)
        # Figure out next sunrise
        if now > sunset:
            tomorrow = today + timedelta(days=1)
            s = sun(CITY.observer, date=tomorrow)
            next_rise = s["sunrise"].replace(tzinfo=None)
        else:
            next_rise = sunrise
        sleep_time = (next_rise - now).total_seconds()
        time.sleep(max(60, sleep_time))
        fade_brightness(NIGHT_LEVEL, DAY_LEVEL)
