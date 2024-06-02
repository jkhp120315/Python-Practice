class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    
    def showDetails(self):
        print("Role -> ", self.role)
        print("Dept -> ", self.dept)
        print("Salary -> ", self.sal)

class Engineer(Employee):
    def __init__(self, role, dept, sal, name, age):
        self.name = name
        self.age = age
        super().__init__(role, dept, sal)
    
    def showEngineerDetails(self):
        print("Name -> ", self.name)
        print("Age -> ", self.age)

e2 = Engineer("Engineer", "Development", 515545.45,"Himanshu",38)
e2.showDetails()
e2.showEngineerDetails()