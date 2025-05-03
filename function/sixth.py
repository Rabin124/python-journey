# def calcSum(a,b):
#   sum = a+b
#   print(sum)
#   return sum

# calcSum(1,2)
# calcSum(11,33)

def add(a,b): #parameters
  return a+b
sum = add(1,2)#arguments
# print(sum)


def print_hello():
  # print("hello")
  pass

print_hello()
print_hello()
print_hello()
print_hello()


def avg(a,b,c):
  sum = a+b+c
  average = sum/3
  # print(average)
  return average

avg(1,2,43)


# recursion
def show(n):
  if(n==0):#base case
    return
  # print(n)
  show(n-1)

show(5)


# factorial

def fact(n):
  if(n==1 or n==0):
    return 1
  return fact(n-1) * n

fact=fact(2)
print(fact)