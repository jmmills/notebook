def changeme(mylist):
    "This changes a passed list into a this function"
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return

mylist = [10,20,30]
print("Values of mylist:", mylist)
changeme(mylist)
print("values ouside the function: ", mylist)
