import time

from Mainclass import Mainclass


class Baseclass:


    def movetoele(self,locator,target):
        time.sleep(2)
        locator.move_to_element(target).perform()

    def selectvals(self,locator,value):

        for ele in range(len(locator)):
            print(locator[ele].text)
            main=Mainclass()
            logs=main.setlogger()
            logs.info(locator[ele].text)
            if locator[ele].text==value:
                locator[ele].click()

