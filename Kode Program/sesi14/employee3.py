class Employee:
 
    def __init__(self, fullname, age, income):
        self.fullname = fullname
        self.age = age
        self.income = income
         
    def func_information(self):
        print('At age', self.age, self.fullname, 'is earning', self.income)
 
class Department(Employee):
     
    def __init__(self, fullname, age, income, dept_name):
        Employee.__init__(self, fullname, age, income)
        self.dept_name = dept_name
 
    def func_info(self):
        print(self.fullname, self.age, 'Working as a',
               self.dept_name, 'is earning', self.income)

emp = Employee('John', '27', '650000')
emp.func_information()
 
print('--------------')
dept = Department('Jenny', '25', '850005', 'Developer')
dept.func_information()
dept.func_info()