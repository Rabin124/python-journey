with open("File InputOutput\\demo.txt", 'r') as f:  # open the file in read mode
    data = f.read()  # read the entire file
    print(data)  # print the data

with open("File InputOutput\\demo.txt", 'w') as f:  # open the file in read mode
    f.write("new data")