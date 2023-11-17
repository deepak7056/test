class employee:
 def __init__(self,name,age,id,salary,inc):
    self.name=name
    self.age=age
    self.id=id
    self.salary=salary
    self.inc=inc
 def comput_total_sal(self):
    print("Total salary with incentive is := ",self.inc+self.salary)
 def emp_details(self):
    print(f"Employee name is {self.name} \n{self.name}'s age is{self.age}\n{self.name}'s salary without incentive is {self.salary} ")
obj1=employee('Deepak',22,3,60000,10000)
print(obj1.emp_details())
print(obj1.comput_total_sal())