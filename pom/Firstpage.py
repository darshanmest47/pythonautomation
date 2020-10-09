import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pom.Covidtracker import Covidtracker
from utilities.Baseclass import Baseclass


class Firstpage:
    projects=(By.XPATH,"//ul[@class='nav-ul']/li[1]")
    contact=(By.XPATH,"//ul[@class='nav-ul']/li[2]")
    title=(By.XPATH,"//span[@class='sp1']")
    react=(By.XPATH,"//h4[contains(text(),'React')]")
    link1=(By.XPATH,"//div[@class='pro1-div']/div[@class='butt-div']/button[3]/a")


    def __init__(self,driver):
        self.driver=driver

    def scrolltotop(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")

    def mouseover1(self):

        acts=ActionChains(self.driver)
        pele=self.driver.find_element(*Firstpage.projects)


        bs=Baseclass()
        bs.movetoele(acts,pele)

    def mouseover2(self):
        acts2=ActionChains(self.driver)
        pele2=self.driver.find_element(*Firstpage.contact)
        bs2 = Baseclass()
        bs2.movetoele(acts2, pele2)

    def switchToFrame1(self):
        self.driver.execute_script("window.scrollTo(0,600)")
        self.driver.switch_to.frame(0)
        assert self.driver.find_element(*Firstpage.title).text == "Covid19-Tracker-India"
        amt=1
        amt2=1
        for ele in range(1,8):

            amt=amt*2
            time.sleep(1)
            self.driver.execute_script(f"window.scrollBy(0,{amt})")

        for ele1 in range(1,8):
            amt2 = amt2 * 2
            time.sleep(1)
            self.driver.execute_script(f"window.scrollBy(0,{-amt2})")

        self.driver.switch_to.default_content()

    def switchToFrame2(self):
        print(self.driver.title)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,1090)")
        self.driver.switch_to.frame(1)

        assert self.driver.find_element(*Firstpage.react).text =="React-Quiz"
        amt = 1
        amt2 = 1
        for ele in range(1, 8):
            amt = amt * 2
            time.sleep(0.5)
            self.driver.execute_script(f"window.scrollBy(0,{amt})")

        for ele1 in range(1, 8):
            amt2 = amt2 * 2
            time.sleep(0.5)
            self.driver.execute_script(f"window.scrollBy(0,{-amt2})")

        self.driver.switch_to.default_content()

    def scrolltoendandtop(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        pros=self.driver.find_element(*Firstpage.projects)
        self.driver.execute_script("arguments[0].scrollIntoView();",pros)
        
    

    def openpro1(self):
        time.sleep(1)
        self.driver.find_element(*Firstpage.link1).click()
        windows=self.driver.window_handles




        self.driver.switch_to.window(windows[1])
        cvd=Covidtracker(self.driver)
        cvd.clicksel()
        cvd.selval()

        for w in windows:
            print(w)
            self.driver.switch_to.window(w)
            print(self.driver.title)
            if self.driver.title=='CovidtrackerIndia':
                self.driver.close()

















