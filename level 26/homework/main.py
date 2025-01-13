# 1)
def sum_of_two_numbers(x, y):
    return x + y
print(sum_of_two_numbers(5, 3))  

# 2)

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(4)) 
print(even_or_odd(7))  

# 3)
def reverse_string(i):
    return i[::-1]
print(reverse_string("GOABEST"))

# 4)

def find_maximum(numbers):
    return max(numbers)
print(find_maximum([1, 2, 3, 4, 5])) 
print(find_maximum([10, 22, 3, 14]))  


# 5)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
print(factorial(5))  
print(factorial(7))  