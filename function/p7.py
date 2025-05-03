def printList(list,inx):
    if inx == len(list):
        return
    print(list[inx])
    printList(list, inx + 1)


list = [ "chitwan",'bhutwal','pokhara','kathmandu']
printList(list, 0)