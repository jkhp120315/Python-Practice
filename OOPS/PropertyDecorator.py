class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def calculateAvg(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
    
s1 =Student(98,97,96)

s1.math = 80
print(s1.calculateAvg)


s1.math = 98
print(s1.calculateAvg)