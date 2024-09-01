#Encapsulation

class SoftwareEngineer:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    self._salary=None
    self._num_bugs_solved=0

#getters
  def get_salary(self):
    return self._salary
#setters
  def set_salary(self,value):
    if value<1000:
      self._salary=1000
    if value >20000:
       self._salary=20000
    self._salary=value

se=SoftwareEngineer("Max",25)
print(se.age,se.name,se._salary)

se.set_salary(5000)
print(se.get_salary())