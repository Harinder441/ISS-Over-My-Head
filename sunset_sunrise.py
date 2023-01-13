import datetime as dt
import requests as req


def sunset_sunrise(lat=29.80435, lng=74.97221, utc=(5, 30, 0)):
    """will return sunset and sunrise as datetime object in 24 hours format"""
    utc_offset = dt.timedelta(hours=utc[0], minutes=utc[1], seconds=utc[2])
    parameters = {
        "lat": lat,
        "lng": lng,
        "formatted": 0,
    }
    res = req.get("https://api.sunrise-sunset.org/json", params=parameters)
    res.raise_for_status()
    data = res.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunset_time = dt.datetime.strptime(sunset.split('+')[0], '%Y-%m-%dT%H:%M:%S') + utc_offset
    sunrise_time = dt.datetime.strptime(sunrise.split('+')[0], '%Y-%m-%dT%H:%M:%S') + utc_offset
    return sunset_time, sunrise_time
