#position,name,age,level,salary

set1=["Software Engineer","mani",20,"Junior",2000]
set2=["Software Engineer","ran",22,"Senior",4000]

class SoftwareEngineer:
  alias="keyboard magician"
  def __init__(self,name,age,level,salary):
    #instance attribute
    self.name=name
    self.age=age
    self.level=level
    self.salary=salary




#instance
set1=SoftwareEngineer("mani",20,"Junior",2000)
print(set1.name,set1.age,set1.level,set1.salary)

print(set1.alias)
set2=SoftwareEngineer("ran",22,"Senior",4000)
print(set2.alias)

#Recape
#create a class (blueprint)
#create an instance(object)
#class Vs Instance
#instance attributes:defined in __init_ _