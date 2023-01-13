from datetime import datetime
from ISS_location import iss_location
from sunset_sunrise import sunset_sunrise
from auto_email import send_mail
from distance import distance
from letter_format import msg_format
import time


UTC_OFSET = (5, 30, 0)
MY_POS = (29.833709, 74.982323)  # Kalanwali
mail_to = "harindersingh2107@gmail.com"
msg_sub = "ISS coming closer"
msg_from = "Internation Space Station"
# MY_POS1 = (-22,-115)
while True:
    time.sleep(60)
    iss_pos = iss_location()
    sunset, sunrise = sunset_sunrise(lat=MY_POS[0], lng=MY_POS[1], utc=UTC_OFSET)
    time_now = datetime.now()
    msg_body = f"Current position {iss_pos}"
    msg = msg_format(from_p=msg_from, body=msg_body, subject=msg_sub)
    is_night = time_now.hour > sunset.hour or time_now.hour < sunrise.hour
    print(distance(iss_pos, MY_POS))
    if distance(iss_pos, MY_POS) < 5 or is_night:
        send_mail(to_ad=mail_to, massage=msg)
        print("massage sent")

