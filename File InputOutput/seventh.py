# File I/O in Python

f=open("D:\\python\\File InputOutput\\demo.txt",'r') # open the file in read mode

# data = f.read()
# data = f.readline()


# print(type(data)) # print the type of data
# print((data)) # print the type of data
line1 = f.readline()
print(line1) # print the type of data
line2 = f.readline()
print(line2) # print the type of data
f.close()