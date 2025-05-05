class Student:
  def __init__(self,name,marks):
    self.name = name
    self.marks = marks

  def get_avg(self):
    sum = 0
    for val in self.marks:
      sum += val
    print("hi",self.name,"your avg score is:",sum/3)
s1 = Student("Ravi Kumar",[99,88,98])
s1.get_avg()  # hi Ravi Kumar your avg score is: 95.0

s1.name = "John Doe"
s1.get_avg()  # hi John Doe your avg score is: 95.0