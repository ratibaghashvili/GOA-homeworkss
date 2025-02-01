# 1

def fucaca():
    print("Hello, World!")
fucaca()


# 2)

def magarikaci(num1,num2):
    print(num1 + num2)

magarikaci(3,99999)


# 3)

def multiply_by_ten(number):
    return number * 10
result = multiply_by_ten(5)
print(result)  
# 4)

def kaia(*number):
    print(number[0]*number[1])
kaia(5,6)


# 5)

def name(name1="greet"):
    print(name1)
name("rati")

# 7)

def even_or_odd(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is odd")
        else:
            print(f"{number} is eaven" )
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_or_odd(list)


# 8)


def find_maximum(numbers):
    if not numbers:
        return None  

    max_number = numbers[0]  
    for number in numbers:
        if number > max_number:
            max_number = number 
    return max_number
numbers_list = [3, 5, 1, 8, 2]
max_num = find_maximum(numbers_list)
print("The maximum number is:", max_num)


# 9)

def get_positive_numbers(lst):
    positive_numbers = []
    for num in lst:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

numbers = [-10, 5, 3, -2, 8, 0]
positive = get_positive_numbers(numbers)
print(positive) 


# 10)

def sum3(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total_sum += num
    return total_sum
result = sum3(1, 100)
print(result)

