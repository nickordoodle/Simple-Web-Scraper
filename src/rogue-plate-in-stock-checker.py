import time
import config

from webbot import Browser
web = Browser()
web.go_to('roguefitness.com/rogue-hi-temp-bumper-plates')

time.sleep(7)

while True:
    if not web.exists('Out of Stock', tag='div', classname='bin-out-of-stock-message'):
        import smtplib
        msg = f'Subject: Rogue Plates Available!!! Go to: https://www.roguefitness.com/rogue-hi-temp-bumper-plates'
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

    web.refresh()
    print('refreshing...')
    time.sleep(5)
