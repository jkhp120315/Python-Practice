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

    def __getBalance(self):
        return self.balance
    
    def callgetBalance(self):
        return self.__getBalance()

a1 = Account("Acc001", 10000)

#print(a1.__getBalance())
print(a1.callgetBalance())