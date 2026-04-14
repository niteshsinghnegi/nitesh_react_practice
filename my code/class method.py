class Employee :
  company="microsoft"
  

  def show (self):
    print(f"the name of employee is : {self.name}and his salray is {self.salary} and company name is : {self.company}")
    
  @classmethod
  def chamgecompany(cls,newcomapany):
      cls.company=newcomapany

e1=Employee()
e1.name="nitesh negi "
e1.salary=100000
e1.age=23
e1.show()
# print(e1.show())
print(Employee.company)
