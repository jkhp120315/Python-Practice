class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height

    @classmethod
    def PersonDetails(cls,name,age,height):
        return cls(name,age,height)

### First use case is to update class level attribute

#a1 = Person()

#a1.UpdateName("Patel")
#print(a1.name)
#print(Person.name)


### 2nd use case is constructor overloading

a2 = Person.PersonDetails("Himanshu",38,5.8)
print("Person name is -> ", a2.name)
print("Person Age is -> ", a2.age)
print("Person height is -> ", a2.height)