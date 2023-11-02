class Employee:

    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary
        self.email = f'{first_name.lower()}.{last_name.lower()}@company.com'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def raise_salary(self):
        self.salary = self.salary * self.raise_amount


class Developer(Employee):

    def __init__(self, first_name, last_name, salary, dev_type):
        # Employee.__init__(self, first_name, last_name, salary)
        super().__init__(first_name, last_name, salary)
        self.dev_type = dev_type

    def write_code(self):
        print(self.full_name(), 'is coding')

class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def list_employees(self):
        if self.employees:
            for employee in self.employees:
                print(employee.full_name())
        else:
            print('You have no employees!')


emp1 = Employee('Jack', 'Smith', 1500)
dev1 = Developer('Mary', 'Gold', 2500, 'frontend')
dev2 = Developer('Bob', 'Summers', 3000, 'backend')
man1 = Manager('Sarah', 'Bond', 5000)

# print(man1.employees)
# man1.add_employee(emp1)
# print(man1.employees)
# man1.add_employee(dev1)
# man1.list_employees()
# print('***')
# man1.remove_employee(dev1)
# man1.list_employees()


print(isinstance(man1, Employee))
print(isinstance(man1, Manager))
print(isinstance(man1, Developer))
print('***')
print(issubclass(Employee, Manager))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))

