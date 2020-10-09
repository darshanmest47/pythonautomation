import time

from selenium.webdriver.common.by import By

from utilities.Baseclass import Baseclass


class Covidtracker:
    def __init__(self,driver):
        self.driver=driver

    selectopts=(By.XPATH,"//select")
    selectvals=(By.XPATH,"//select/option")
    stval=(By.XPATH,"//div[@class='card-title']/h5/span")


    def clicksel(self):
        time.sleep(0.5)
        self.driver.find_element(*Covidtracker.selectopts).click()

    def selval(self):
        time.sleep(0.5)

        vals=self.driver.find_elements(*Covidtracker.selectvals)
        bsc=Baseclass()
        bsc.selectvals(vals,'Karnataka')

        assert self.driver.find_element(*Covidtracker.stval).text=="State: Karnataka"


