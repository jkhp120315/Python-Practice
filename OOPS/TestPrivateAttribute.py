class Account:

    def __init__(self,accountid, balance):
        self.__accountid = accountid
        self.balance = balance

    def debit(self,debitAmt):
        self.balance = self.balance - debitAmt
        print("Rs. ", debitAmt, "debited")

    def credit(self,creditAmt):
        self.balance = self.balance + creditAmt
        print("Rs. ", creditAmt, "Credited")

    def getBalance(self):
        return self.balance
    
    def setAccountId(self,accountId):
        self.accountId = accountId

a1 = Account("Acc001", 10000)

print(a1.__accountid)

