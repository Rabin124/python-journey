count =0
with open("File InputOutput\\practice.txt", 'r') as f:  # open the file in read mode
    data = f.read()  # read the entire file
    print(data)  # print the data

    # num = ""
    # for i in range(len(data)):
    #     if data[i] == ",":
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count +=1

print("even numbers count",count)