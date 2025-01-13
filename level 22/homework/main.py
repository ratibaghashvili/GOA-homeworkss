# 1)

# slicing-არის მოცემული ლისტის "დაჭრა"- დაწილება

# 2)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in my_list:
    print(i)


# 3)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


num1 = int(input("enter first number: "))
num2 = int(input("enter second number : "))

if num1 > num2:
    slist = my_list[num1:num2]
    print(list)
elif num2 > num1:
    list1 = my_list[num2:num1]
    print(list1)
else:
    print([]) 


# 4)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numbers[0])  
print(numbers[2])  
print(numbers[-1])  

# 5)


fruit = ["apple", "banana", "orange", "mango", "berry"]

reversed = fruit[::-1]
print(reversed)

# 6)


fruit = ["apple", "banana", "orange", "mango", "berry", "cherry", "grape", "avocado"]

fruit1 = fruit[::2]
print(fruit1)

# 7)

