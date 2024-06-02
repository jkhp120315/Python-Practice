class Person:
    name = "himanshu"

    #def changeName(self,name):
    #    self.name = name

    @classmethod
    def UpdateName(cls,name):
        cls.name = name

a1 = Person()

a1.UpdateName("Patel")
print(a1.name)
print(Person.name)
