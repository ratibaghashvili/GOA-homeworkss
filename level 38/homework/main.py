# 1)
tuple = (10, 20, 30, 40, 50)
second_element = tuple[1]
last_element = tuple[-1]

mid_slice = tuple[1:4]

print("second element:", second_element)
print("last element:", last_element)
print("middle slice:", mid_slice)


# 2)

my_tuple = (10, 20, 30)
my_tuple[1] = 99
# this will send erorr

# 3)


my_tuple = (1, 'bagha', 3.1767, True)

a, b, c, d = my_tuple
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


# 4)

tuple = (1, 2, 3, 2, 4, 2)
count2 = tuple.count(2)
index2 = tuple.index(2)
print("count of 2:", count2)
print("cndex of 2:", index2)


# 5)


my_set = {1, 2, 3, 4, 5}
my_set.add(6)
my_set.remove(3)
is_present = 4 in my_set
print("set after operations:", my_set)
print("is 4 present in the set?", is_present)


# 7 )

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

# 8)

list_rati = [1, 2, 3, 4, 4, 5, 5, 6,6]
list_rati = list(set(list_rati))
print(list_rati)