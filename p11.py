# wap to grade students based on marks

marks = float(input("Enter the marks: "))

if(marks >= 90):
  print("grade = 'A'")
elif(90 > marks >= 80):
  print("grade = 'B'")
elif(80 > marks >= 70):
  print("grade = 'C'")
else:
  print("grade = 'D'")