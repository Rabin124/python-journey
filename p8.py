a = int(input("Enter a side of triangle: "))
b = int(input("Enter b side of triangle: "))
c = int(input("Enter c side of triangle: "))
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is: ",area)
