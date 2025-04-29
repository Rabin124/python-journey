# wap to find the greatest of 3 numbers entered by the user

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if((a>=b) and (a>=c)):
  print(a," is greater number")
elif(b>=c):
  print(b," is greater number") 
else:
  print(c," is greater number") 