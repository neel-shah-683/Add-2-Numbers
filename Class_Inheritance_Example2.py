class Employee:
    salary = 500
    increment = 100

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sai):
        self.increment = sai / self.salary

e = Employee()
print(e.salaryAfterIncrement)


         
