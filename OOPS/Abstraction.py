from abc import ABCMeta, abstractmethod
class BankApp(metaclass=ABCMeta):

    @abstractmethod
    def connectDatabase(self):
        pass


class MobileApp(BankApp):
    def startMobileApp(self):
        print("Mobile app is starting..")

p1 = BankApp()