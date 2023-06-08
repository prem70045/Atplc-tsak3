num_list = []
for i in range(10):
    num = int(input("Enter an integer: "))
    num_list.append(num)

reverse_list = num_list[::-1]


print("Original list:", num_list)
print("Reversed list:", reverse_list)
