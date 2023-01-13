import requests as req


def iss_location():
    """will return a tuple (latitude , longitude)"""
    res = req.get(url="http://api.open-notify.org/iss-now.json")
    res.raise_for_status()
    data = res.json()
    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])
    iss_pos = (latitude, longitude)
    return iss_pos
