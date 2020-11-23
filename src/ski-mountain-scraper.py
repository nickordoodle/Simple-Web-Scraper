# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),
from requests import Session

while True:


    from requests import Session
    from bs4 import BeautifulSoup as bs

    with Session() as s:
        site = s.get("https://www.epicpass.com/account/login")
        bs_content = bs(site.content, "html.parser")
        token = bs_content.find("input", {"name": "csrf_token"})["value"]
        login_data = {"username": "nscherer30@gmail.com", "password": "Gummybear30#)", "csrf_token": token}
        s.post("https://www.epicpass.com/account/login", login_data)
        home_page = s.get("https://www.epicpass.com/account")
        print(home_page.content)

print("change")
