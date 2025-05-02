num = (1,4,9,16,25,36,49,64,81,100)

x =36
idx = 0
while idx < len(num):
  if(num[idx] == x):
    print("Found at idx", idx)
    break
  else:
    print("finding...")
  idx +=1