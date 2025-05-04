def check_for_line():
  word = "learning"  # string to be written to the file
  data =True
  line_no =1
  with open("File InputOutput\\practice.txt", 'r') as f:  # open the file in read mode
    while data:
      data = f.readline()
      if(word in data):
        print("word found in line",line_no)
        return
      line_no +=1


  return -1


check_for_line()