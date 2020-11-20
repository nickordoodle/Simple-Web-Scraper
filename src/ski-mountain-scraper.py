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
        #
        #
        #
        # # Search and Email Notifications
        #
        # # set the url as VentureBeat,
        # url = "https://www.epicpass.com/plan-your-trip/lift-access/reservations.aspx"
        # # set the headers like we are a browser,
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        # # download the homepage
        # response = requests.get(url, headers=headers)
        # # parse the downloaded homepage and grab all text, then,
        # soup = BeautifulSoup(response.text, "lxml")
        #
        # # if the number of times the word "Google" occurs on the page is less than 1,
        # if str(soup).find("Choose the Date") == -1:
        #     # wait 60 seconds,
        #     time.sleep(20)
        #     # continue with the script,
        #     continue
        #
        # # but if the word "Google" occurs any other number of times,
        # else:
        #     # create an email message with just a subject line,
        #     msg = 'Subject: [CHECK EPIC PASS RESERVATIONS!] This is Nick\'s peculiar brain talking, [CHECK EPIC PASS RESERVATIONS!]'
        #     # set the 'from' address,
        #     fromaddr = 'nscherer30@gmail.com'
        #     # set the 'to' addresses,
        #     toaddrs = ['nick.d.scherer@gmail.com']
        #
        #     # setup the email server,
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.starttls()
        #     # add my account login name and password,
        #     server.login("nscherer30@gmail.com", "dmrwbuzdfdblmrxf")
        #
        #     # Print the email's contents
        #     print('From: ' + fromaddr)
        #     print('To: ' + str(toaddrs))
        #     print('Message: ' + msg)
        #
        #     # send the email
        #     server.sendmail(fromaddr, toaddrs, msg)
        #     # disconnect from the server
        #     server.quit()
        #
        #     break

