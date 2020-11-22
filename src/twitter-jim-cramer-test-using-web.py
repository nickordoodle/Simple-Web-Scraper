import time
from webbot import Browser

web = Browser()
web.go_to('twitter.com/jimcramer')

time.sleep(6)

resultElements = web.find_elements(text='concepts', tag='span')

testKeyMatch = 'concepts'

for element in resultElements:
    print(element.text)
    if(element.text.contains(testKeyMatch)):
        #match found


    print(element.tag_name)
    print(element.parent)
    print(element.location)
    print(element.size)
