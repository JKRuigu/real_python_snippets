class Employee:
    #instancevariable
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first_name, last_name, pay):
        #classattributes, #Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + last_name + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{}{}".format(self.first_name, self.last_name)
    #classvariable
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        return self.pay
    
    #classmethods
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

#setinstancesofclass

emp_1 = Employee("Waithira", "Kunene", 78000)
emp_2 = Employee("John", "Kamau",70000)

print (Employee.fullname(emp_1))
print (Employee.raise_amount)

print (Employee.num_of_emps)