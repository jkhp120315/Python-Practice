class Student:

    def __init__(self,name,subjectmarks):
        self.name = name
        self.subjectmarks = subjectmarks
    
    def calculateAvg(self):
        totalMarks = 0
        for i in self.subjectmarks:
            totalMarks = totalMarks + i
        
        avgMarks = totalMarks / 3

        return avgMarks
    
s1=Student("Himanshu",[100,99,91])
print("Student",s1.name, "has got avg ", s1.calculateAvg(),"in 3 subjects")

s1.name = "Jaimin"
s1.subjectmarks = [100,99,99]
print("Student",s1.name, "has got avg ", s1.calculateAvg(),"in 3 subjects")
