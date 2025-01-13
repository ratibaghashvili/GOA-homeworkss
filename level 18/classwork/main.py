# 1)
for i in range(0, 21, 2):
    print(i)
# 2)
for i in range(1, 21, 2):
     print(i)

for i in range(10, 31):
    if i % 2 == 0:
        print(str(i), "-even")
else:
        print(str(i)), "-odd"




num1 = int(input("type first number: "))
num2 = int(input("type second number: "))


if num1 > num2:

    even_numbers = [i for i in range(num2, num1 + 1) if i % 2 == 0]
    print("even numbers:", even_numbers)
    total = sum(even_numbers) 
else:

    odd_numbers = [i for i in range(num1, num2 + 1) if i % 2 != 0]
    print("odd numbers:", odd_numbers)
    total = sum(odd_numbers) 


print("number total:", total)