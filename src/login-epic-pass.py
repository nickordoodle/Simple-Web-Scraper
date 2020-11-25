import time
import myConfig

from webbot import Browser
web = Browser()
web.go_to('epicpass.com/account/login')
web.type(myConfig.fromEmail, into='EMAIL')
web.type(myConfig.epicLoginPass, into='PASSWORD', id='passwordFieldId')
web.click('SIGN IN' , tag='button')
#logged in now

daysToReserve = ['26', '27', '28', '29']

web.go_to('epicpass.com/plan-your-trip/lift-access/reservations.aspx')

while True:
    time.sleep(2)
    web.click('Park City', tag='option')
    web.click('CHECK AVAILABILITY', tag='button')
    for day in daysToReserve:
        # Check to see if day is available
        isDayAvailable = web.exists(day, tag='button', classname='passholder_reservations__calendar__day--disabled')
        if not isDayAvailable:
            import smtplib
            msg = f'Subject: NOV {day} IS OPEN!!! https://www.epicpass.com/plan-your-trip/lift-access/reservations.aspx'
            # set the 'from' address,
            fromaddr = myConfig.fromEmail
            # setup the email server,
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # add my account login name and password,
            server.login(fromaddr, myConfig.gmailLoginAppPass)
            # Print the email's contents
            print('From: ' + fromaddr)
            print('To: ' + str(myConfig.emailList))
            print('Message: ' + msg)
            # send the email
            server.sendmail(fromaddr, myConfig.emailList, msg)
            # disconnect from the server
            server.quit()
        else:
            print(f'{isDayAvailable} epic pass day not available.')

    web.click('Okema', tag='option')
    web.click('CHECK AVAILABILITY', tag='button')