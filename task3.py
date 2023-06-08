def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [5, 10, 15, 20]

print(common_member(list1, list2))
print(common_member(list1, list3))
