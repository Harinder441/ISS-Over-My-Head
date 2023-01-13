import smtplib


def send_mail(to_ad, massage,from_ad=Your_email_id, password=Your_APP_password):
    with smtplib.SMTP("smtp.gmail.com") as con:
        # securing
        con.starttls()
        # login
        con.login(user=from_ad, password=password)
        con.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=massage)


if __name__ == "__main__":
   pass
