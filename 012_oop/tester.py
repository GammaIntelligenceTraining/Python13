import datetime

class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary
        self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'
        Employee.number_of_employees += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def raise_salary(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def change_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def employee_from_string(cls, emp_string):
        first_name, last_name, salary = emp_string.split('-')
        return cls(first_name, last_name, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]:
            return False
        return True


# print(Employee.number_of_employees)
emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee.employee_from_string('MAX-POWER-2500')
# emp2 = Employee()
#
# print(emp1)
# print(emp2)
#
# emp1.first_name = 'Jack'
# emp1.last_name = 'Smith'
# emp1.salary = 2000
#
# print(emp1.first_name, emp1.last_name, emp1.salary)
# print(emp1.email)
# print(emp1.full_name())
# print(Employee.full_name(emp1))
# print(emp1.__dict__)
# print(Employee.__dict__)
#
# print(Employee.number_of_employees)
# print(emp1.number_of_employees)
print(emp1.salary)
# emp1.raise_amount = 1.15
emp1.change_raise_amount(1.10)
emp1.raise_salary()
print(emp1.salary)

print(emp2.full_name())

print(emp1.__dict__)
print(Employee.__dict__)

dt = datetime.date.today()
print(Employee.is_workday(dt))
print(emp1.is_workday(dt))