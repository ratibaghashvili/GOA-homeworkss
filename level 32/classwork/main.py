def generate_big_sentence(name, surname, age):

    print("My name is {}, my surname is {}, and I am {} years old.".format(name, surname, age))


name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = input("Please enter your age: ")

generate_big_sentence(name, surname, age)


def generate_big_sentence(name, surname, age):

    print(f"My name is {name}, my surname is {surname}, and I am {age} years old.")


name = input("Please enter your name: ")
surname = input("Please enter your surname: ")
age = input("Please enter your age: ")

generate_big_sentence(name, surname, age)


def my_split(main_string, string_to_split):
    result = main_string.split(string_to_split)
    print(result)
main_string = input("enter the  string: ")
string_to_split = input(" enter the string to split : ")

my_split(main_string, string_to_split)



def manual_append(main_list, item_to_insert):
    
    main_list.insert(len(main_list), item_to_insert)
my_list = [1, 2, 3, 4]
item = 5
manual_append(my_list, item)
print(my_list)