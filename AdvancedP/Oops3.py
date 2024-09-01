#inherits ,extend, override

# class Employee:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

#   def work(self):
#     print(f"{self.name} is working..")

# class SoftwareEngineer(Employee):
#   pass

# class Designer(Employee):
#   pass

# se=SoftwareEngineer("Max",25)
# se.work()

# d=Designer("Philips",23)
# d.work()


#Extends
# class Employee:
#   def __init__(self,name,age,salary,level):
#     self.name=name
#     self.age=age
#     self.salary=salary

#   def work(self):
#     print(f"{self.name} is working..")

# class SoftwareEngineer(Employee):
#   def __init__(self,name,age,level,salary):
#     super().__init__(name,age,level,salary)
#     self.level=level
#     self.salary=salary

#     def debug(self):
#         print(f"{self.name} is debugging..")



# class Designer(Employee):
#   pass

# def draw(self):
#     print(f"{self.name} is drawing..")


# se=SoftwareEngineer("Max",25,6000,"Junior")
# se.work()
# se.debug()
# se.draw()
# print(se.level)

# d=Designer("Philips",23,7000,"Senior")
# d.work()
# d.draw()


#Override

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


