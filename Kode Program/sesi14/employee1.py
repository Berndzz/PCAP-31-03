class Employee:
 
    def __init__(self, fullname, age, income):
        self.fullname = fullname
        self.age = age
        self.income = income
 
    def func_msg(self):
        print('Welcome to Employee Class')
         
    def func_information(self):
        print('At age', self.age, self.fullname, 'is earning', self.income)
 
class Department(Employee):
    pass
 
emp = Employee('Suresh', '27', '650000')
emp.func_msg()
emp.func_information()
 
print('--------------')
dept = Department('Jenny', '25', '850005')
dept.func_msg() # Calling Parent Method func_msg(self)
dept.func_information() # Calling Parent Method func_information(self)