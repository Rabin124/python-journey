class Student:
  college = "ABC College"
  # parameterized constructor
  def __init__(self,fullname,marks):
    self.name = fullname
    self.marks = marks
    print("adding new student..")


  # # default constructor
  # def __init__(self):
  #   pass

  def welcome(self):
    print("Welcome to the class",self.name)

  def get_marks(self):
    return self.marks

s1 = Student("Ravi Kumar",33)

print(s1.name, s1.marks)  # Ravi Kumar

s2 = Student("John Doe",99)
print(s2.name, s2.marks)  # John Doe

print(Student.college)  # ABC College

s1.welcome()
print(s1.get_marks())  # 33