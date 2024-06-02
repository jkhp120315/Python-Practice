class Account:

    def __init__(self,accountid, balance):
        self.accountid = accountid
        self.balance = balance

    def debit(self,debitAmt):
        self.balance = self.balance - debitAmt
        print("Rs. ", debitAmt, "debited")

    def credit(self,creditAmt):
        self.balance = self.balance + creditAmt
        print("Rs. ", creditAmt, "Credited")

    def getBalance(self):
        return self.balance

a1 = Account("Acc001", 10000)
print("Total Balance", a1.getBalance())

a1.debit(5000)
print("Total Balance", a1.getBalance())

a1.credit(15000)
print("Total Balance", a1.getBalance())