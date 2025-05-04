word = "learning"  # string to be written to the file
with open("File InputOutput\\practice.txt", 'r') as f:  # open the file in read mode
    data = f.read()  # read the entire file
    if(data.find(word) != -1):
        print("word found")
    else:
        print("word not found")