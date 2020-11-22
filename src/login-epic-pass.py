import time

from webbot import Browser
web = Browser()
web.go_to('epicpass.com/account/login')
# web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
# web.press(web.Key.ENTER)
# web.go_back()
# web.click('Sign in')
web.type('nscherer30@gmail.com' , into='EMAIL')
# web.type('mypassword' , into='PASSWORD', id='passwordFieldId')
web.type('Gummybear30#)' , into='PASSWORD', id='passwordFieldId')
web.click('SIGN IN' , tag='button') # you are logged in . oohoooo


time.sleep(5)

web.go_to('epicpass.com/plan-your-trip/lift-access/reservations.aspx')


web.click('Park City' , tag='option')


time.sleep(2)

web.click('CHECK AVAILABILITY' , tag='button')



#--------------------------------------------------------------------------

# # If multiple buttons with similar properties are to be clicked at once
# web = Browser()
# web.go_to('siteurl.com')
# web.click('buttontext' , multiple = True)
#
# #--------------------------------------------------------------------------
#
# # If there are multiple elements and you want to perform action on one of them :
# web = Browser()
# web.go_to('siteurl.com')
#
# # types the text into the 3rd input element when there are multiple input elements with form-input class
# web.type('im robo typing' , number = 3 , classname="form-input" )