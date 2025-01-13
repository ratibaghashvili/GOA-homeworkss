# 1)

# elif არის დამატებითი პირობა, რომელიც შემოწმდება მხოლოდ მაშინ როცა წინა if არ შესრულდა ან არიმუშავა,elif ყოველთვის იწერება if ის მერე

# 2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1

elif num2 >= num1 and num2 >= num3:
    largest = num2

else:
    largest = num3

print(largest)


# 3)


score = int(input("enter score (0-100): "))

if 90 <= score <= 100:
    print("score: A")

elif 80 <= score <= 89:
    print("score: B")

elif 70 <= score <= 79:
    print("score: C")

elif 60 <= score <= 69:
    print("score: D")
    
else:
    print("score: F")


# 4)

num=int(input("enter a number"))

if num > 0:
    print("number is positive")

elif num < 0:
    print("number is negative")

else:
    print("number is zero")


# 5)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

any_numbers = 0


for num in range(start, end + 1):
    any_numbers += num

# Print the sum
print(any_numbers)


# 6)

def is_prime(number):
  
    if number <= 1:
        return False

    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
      
        if number % i == 0 or number % (i + 2) == 0:
            return False

        i += 6

    return True

number = int(input("შეიყვანეთ რიცხვი: "))

if is_prime(number):
    print(number)
else:
    print(number)
