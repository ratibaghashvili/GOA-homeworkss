# 1)

list1 = [1, 2, 3, 4, 5, "a", "b", True, False, 3.5]
user_number = int(input("Enter number: "))

if 0 <= user_number and user_number < 10: print(list1[user_number])
elif user_number >= -10 and user_number <= -1: print(list1[user_number])
else: print("Wrong index")

# 2)

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list1:
    print(x*2)
    print(x/2)