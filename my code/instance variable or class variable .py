class School:
    college_name = "saraswati vidya mandir brijilok"
    no_of_employees = 0

    def __init__(self, name):
        self.name = name
        self.salary_amount = 3200
        School.no_of_employees += 1

    def showDetails(self):
        print(f"The name of the employee is {self.name}, salary amount is {self.salary_amount}, "
              f"college name is {School.college_name}")

    @classmethod
    def showTotalEmployees(cls):
        print(f"Total number of employees is {cls.no_of_employees}")

# Create employees
emp1 = School("Mr. Naresh Chandra ji")
emp1.salary_amount = 21000
emp1.showDetails()

emp2 = School("Mr. Pradeep Pandey ji")
emp2.salary_amount = 17000
emp2.showDetails()

emp3 = School("Mr. Home Singh ji")
emp3.salary_amount = 7000
emp3.showDetails()

emp4 = School("Mr. Pankaj ji")
emp4.salary_amount = 18000
emp4.showDetails()

# Show total employees
School.showTotalEmployees()
