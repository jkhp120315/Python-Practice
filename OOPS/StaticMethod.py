
class Student:

    def __init__(self,name):
        self.name = name

    @staticmethod
    def printCollegeName(college):
        print("College Name is ", college)
    
    def printStudentName(self):
        print("Student Name is ", self.name)
    

s1 = Student("Himanshu")
Student.printCollegeName("IIT Powai") # This works fine as this is static method
s1.printCollegeName("IIM Ahemedabad")
#Student.printStudentName() # This fails as this is instance method

s1.printStudentName() # This works fine as this is Instance method