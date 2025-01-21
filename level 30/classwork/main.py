
name = input(" enter your name: ")


choice = input("enter 'u'  uppercase or 'l' lowercase: ")

if choice == "u":
    print(name.upper())  
elif choice == "l":
    print(name.lower()) 
else:
    print("wrong")  


def manual_find(main_strong,str_to_find):
    print(main_strong.find(str_to_find))

main_strong = input("sumbit : ")
str_to_find = input("finder: ")
manual_find(main_strong,str_to_find)





main_str = input("enter string: ")

str_to_count = input("enter count string: ")


count = main_str.count(str_to_count)

print(str_to_count,main_str, count)



def manual_spawcase(main_str):
    res + ""

    for char in main_str:
        if char.islower(): res += char.upper()
        else: res += char.lower()
    print(res)

manual_spawcase("kaikacikaikaci")
print("kaikacikaikaci".swapcase())
