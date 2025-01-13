#  1)

#პირობითი განცხადებები  პროგრამირებაში გამოიყენება იმისთვის რომ პროგრამამ განსხვავებული მოქმედებები შეასრულოს სხვადასხვა პირობების მიხედვით.
#პირობითი განცხადებების ერთერტი ტიპი არის if-else:
# პირობა აკმაყოფილებს (True) მაშინ შესრულდება პირველი მოქმედება if
# არ აკმაყოფილებს (False) მაშინ შესრულდება მეორე მოქმედება else

# 2)

first_num = int(input("ENTER FIRST NUMBER: "))
second_num = int(input("ENTER SECOND NUMBER : "))
if first_num > second_num:
    print(first_num)
else:
    print(second_num)

# 3)

num = int(input("enter number: "))

if num % 2 == 0:
    print("your number is Even")
else:
    print("your number is Odd")


# 4)


number = float(input("მიუთითეთ რიცხვი: "))

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else: 
    print("number is zero")

# 5)


number = int(input("enter number: "))


if number % 5 == 0:
    print("The number is divisible by 5 without a remainder")
else:
    print("The number is not divisible by 5")

# 6)

for i in range(5):
  
    number = int(input("Enter a number: "))
    
   
    if number % 2 == 0:
        print(str(number) + " is Even" )
    else:
        print(str(number) + " is Odd")


# 7)

# for loop-ი გამოიყენება მაშინ, როდესაც ჩვენ ვიცით იტერაციების რაოდენობა
# while loop-ი გამოიყენება მაშინ, როდესაც ჩვენ არ ვიცით იტერაციების რაოდენობა

password = "goa_best"
user_password = input("Please enter a password: ")
tries = 1

while user_password != password:
    print("Password is incorrect!")
    user_password = input("Please enter a password: ")
    tries += 1
    
print("Password is correct!")
print("You required " + str(tries) + " tries")

# 8)


num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(int(num1 + num2))
elif operator == "-":
    print(int(num1 - num2))
elif operator == "*":
    print(int(num1 * num2))
elif operator == "/":
    if num2 != 0:
        print(int(num1 / num2))
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator!")