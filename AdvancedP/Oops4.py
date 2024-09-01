#Polymorphism
class Employee:
  def __init__(self,name,age,salary,level):
    self.name=name
    self.age=age
    self.salary=salary

  def work(self):
    print(f"{self.name} is working..")

class SoftwareEngineer(Employee):
  def __init__(self,name,age,level,salary):
    super().__init__(name,age,level,salary)
    self.level=level
    self.salary=salary

    def debug(self):
        print(f"{self.name} is debugging..")

    def code(self):
        print(f"{self.name} is coding..")


    def design(self):
        print(f"{self.name} is designing..")

    def draw(self):
        print(f"{self.name} is drawing..")

class Designer(Employee):
  pass

def design(self):
    print(f"{self.name} is designing..")



def draw(self):
    print(f"{self.name} is drawing..")


se=SoftwareEngineer("Max",25,6000,"Junior")
se.work()


d=Designer("Philips",23,7000,"Senior")
d.work()

employee=[SoftwareEngineer("Max",25,3000,"Junior"),
          SoftwareEngineer("lisa",29,4000,"Senior"),
          Designer("Philips",27,20000)]

def motivate_employee(employees):
  for employee in employees:
    employee.work()

motivate_employee(employee)