mylist = [1, 2, 3, 4, 5, 65, 67, 7, 87, 8, 8, 88, 8, 86, 33, 454, 543, 43, 543, 543, 3, 5, 34, 34, 53, 5, 4, 5, 435, 4, 4, 54, 3]
print(len(mylist))

for i in range(0, len(mylist), 4):
    for j in range(i, i+4):
        if j < len(mylist):
            print(mylist[j])