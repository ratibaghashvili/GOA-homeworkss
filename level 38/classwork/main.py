# 1
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for index in range(len(tuple1)):
    print(tuple1[index])

# 2)

def no_duplicates(user_list):
    return list(set(user_list))
print(no_duplicates([1, 2, 2, 3, 4, 4]))  
print(no_duplicates([5, 5, 5, 5, 5]))
print(no_duplicates([10, 20, 30, 20, 10]))  