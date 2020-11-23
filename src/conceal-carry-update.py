import time

from webbot import Browser
web = Browser()
web.go_to('kiosk.na1.qless.com/kiosk/app/home')

time.sleep(5)

web.type('Nicholas' , into='First name:')
web.type('Scherer' , into='Last name:')
web.type('9735808051' , into='Cell Phone:')

web.click('Next' , tag='button')

web.click('Records Unit' , tag='button', id='btnQueue_100100000746')

web.click('CPL Applications' , tag='button')



