#position,name,age,level,salary

set1=["Software Engineer","mani",20,"Junior",2000]
set2=["Software Engineer","ran",22,"Senior",4000]
d1=["Designer","philips"]



class SoftwareEngineer:
  alias="keyboard magician"
  def __init__(self,name,age,level,salary):
    #instance attribute
    self.name=name
    self.age=age
    self.level=level
    self.salary=salary

#instance method
def code(self):
  print(f"{self.name} is writing code...")

def code_in_language(self,language):
  print(f"{self.name}  is writing code in {language}...")

def information(self):
  information=f"name={self.name},age={self.age},level={self.level}"
  return information

#dunder method()
def __str__(self):
  information=f"name={self.name},age={self.age},level={self.level}"
  return information

def __eq__(self,other):
  return self.name==other.name and self.age==other.age

@staticmethod
def entry_salary(age):
  if age<25:
    return 5000
  if age<30:
    return 7000
  return 9000


se1=["Software Engineer","mani",20,"Junior",2000]
se2=["Software Engineer","rani",22,"Senior",4000]
se3=["Software Engineer","Anita",25,"Senior",40000]

se1.code()
se2.code()
se1.code_in_language("Python")
se1.code_in_language("Java")

print(se1.entry_salary(23))
print(SoftwareEngineer.entry_salary(24))

print(se1)
print(se2)


#instance
set1=SoftwareEngineer("mani",20,"Junior",2000)
print(set1.name,set1.age,set1.level,set1.salary)

print(set1.alias)
set2=SoftwareEngineer("ran",22,"Senior",4000)
print(set2.alias)

#Recape
#instance method(self)
#can take arguments and can return arguments
#special "dunder"method(__str__and __eq__)
#@staticmethod