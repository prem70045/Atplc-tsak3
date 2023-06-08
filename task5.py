my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
indexes_to_remove = [0, 4, 5]

for i in sorted(indexes_to_remove, reverse=True):
    del my_list[i]

print(my_list)
