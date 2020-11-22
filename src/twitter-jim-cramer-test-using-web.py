import time
import config
from webbot import Browser

web = Browser()
web.go_to('twitter.com/jimcramer')

time.sleep(6)

resultElements = web.find_elements(text='concepts', tag='span')

testKeyMatch = 'concepts'

for element in resultElements:
    print(element.text)
    if testKeyMatch in element.text:
        #match found
        # Import requests (to download the page)
        import requests

        # Import smtplib (to allow us to email)
        import smtplib

        # while this is true (it is true by default),
        while True:
            msg = f'Subject: Found {testKeyMatch} from Jim Cramer Tweet.  Full Tweet below'
            # set the 'from' address,
            fromaddr = config.fromEmail


            # setup the email server,
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # add my account login name and password,
            server.login(fromaddr, config.gmailLoginAppPass)

            # Print the email's contents
            print('From: ' + fromaddr)
            print('To: ' + str(config.emailList))
            print('Message: ' + msg)

            # send the emai
            server.sendmail(fromaddr, config.emailList, msg)
            # disconnect from the server
            server.quit()

            break




    print(element.tag_name)
    print(element.parent)
    print(element.location)
    print(element.size)
