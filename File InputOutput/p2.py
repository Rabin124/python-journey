with open("File InputOutput\\practice.txt", 'r') as f:  # open the file in read mode
    data = f.read()  # read the entire file

new_data = data.replace("Java", "Python")  # replace the string "I" with "You"

print(new_data)  # print the data

with open("File InputOutput\\practice.txt", 'w') as f: 
    f.write(new_data)  # write the new data to the file