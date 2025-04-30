# lists 
marks = [11,22,33,44]
bio = ["Rabin", 12.22, True, 25 , "Nepal"]
# print(bio)
bio[0]= "nanu"
# print(bio)
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# list slicing
num = [86,55,22,77,55,45]
# print(num[:4])
# print(num[1:])
# print(num[-3:-1])

# list methods
list = [2,1,3]
list.append(4)
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(1,5)
list.remove(5)
list.pop(3)
# print(list)

# list -> mutable
# string -> tuple -> immutable
# tuples in python

tup = (2,1,3,1)
# print(type(tup))
# print(tup[0])
# print(tup[1:3])
print(tup.index(2))
print(tup.count(2))
