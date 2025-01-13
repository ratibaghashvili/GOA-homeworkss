list = [1, 2, 3, 4, 5]
first_element = list[0]
print(first_element)

list = [10, 20, 30, 40, 50]
last_element = list[-1]
print(last_element)

list = [10, 20, 30, 40, 50]
first_three_elements = list[:3]
print(first_three_elements)

rati = "GoaBest"
last_five = rati[-5:]
print(last_five)

nikusha = "GOABEST"
reversed_string = nikusha[::-1]
print(reversed_string)

list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
every_third_element = list[::3]
print(every_third_element)


list = [10, 20, 30, 40, 50, 60]
half_1 = list[:len(list)//2]  
half_2 = list[len(list)//2:]  

print("First half:", half_1)
print("Second half:", half_2)