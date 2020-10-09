from Mainclass import Mainclass
from pom.Firstpage import Firstpage


class Testproto(Mainclass):



    def test_first(self):
        print('Opened')
        fp=Firstpage(self.driver)
        fp.scrolltotop()
        fp.mouseover1()
        fp.mouseover2()

    def test_second(self):
        fp1=Firstpage(self.driver)
        fp1.switchToFrame1()

    def test_third(self):
        fp2=Firstpage(self.driver)
        fp2.switchToFrame2()

    def test_fourth(self):
        fp3=Firstpage(self.driver)
        fp3.scrolltoendandtop()

    def test_five(self):
        fp4=Firstpage(self.driver)
        fp4.openpro1()

