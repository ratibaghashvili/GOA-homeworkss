# 1 )

# format ფუნქცია არის მეთოდი, რომელიც საშუალებას აძლევს მომხმარებელს შეავსოს სტრინგი კონკრეტული მნიშვნელობებით. ეს ფუნქცია გამოიყენება სტრინგზე, რომელსაც აქვს {} ადგილები, რომლებსაც უნდა მიაწვდონ მნიშვნელობები.
# f-string არის  ფუნქცია, რომელიც საშუალებას აძლევს პირდაპირ სტრინგში ჩაწეროთ ცვლადები და გამოხატულებები {} , როდესაც სტრინგი იწყება f ან F ასოებით.
# f-string უფრო კარგი და მარტივი მიგომმაა
# append და insert ორივე მეთოდი გამოიყენება სიაში ელემენტების დამატებისთვის, მაგრამ მათი მოქმედება განსხვავებულია.

# 2)

def user(age , name):
    return f"welcome your age is {age} and name is {name}"

user_age = int(input("enter your age: "))
user_name = input("enter your name : ")
iasnia = user(user_age , user_name)
print(iasnia) 


# 3)

def format_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    return f"{first_name} {last_name}"

first = input("enter your first name: ")
last = input("enter your last name: ")
full = format_name(first, last)
print("formatted Name:", full)

# 4)

def reverse_string(text):
    reversed_text = text[::-1]  
    return f"reversed string is: {reversed_text}"

# Example usage:
print(reverse_string("Goa is best academy"))


# 5)

def word1(sentence, word, index):
    words = sentence.split() 
    words.insert(index, word)  
    return ' '.join(words)  

print(word1("i love goa academy", "index.html", 2))


# 6)

def toooo(sentence):
    return sentence.split()  
print(toooo("I love Goa"))


# 7)

def list(string):
    return string.split(',') 

print(list("rati,oto,toko"))


# 8)

def split_paragraph(paragraph):
    return paragraph.split('.')  

print(split_paragraph("dzaaan magaria programireba. kaikaci aris rati."))

# 9)


def list(my_list, item):
    my_list.append(item)  
    return my_list

print(list([1, 2, 3], 4))


# 10)

def append1(my_list, items):
    my_list.extend(items) 
    return my_list

print(append1[1, 2, 3], [4, 5, 6])


# 11)

def append(list1, list2):
    list1.extend(list2) 
    return list1
print(append([1, 2], [3, 4]))


# 12)

def insert_item(my_list, index, item):
    my_list.insert(index, item)  
    return my_list
print(insert_item([1, 2, 3], 1, 4))


# 13)

def insert(my_list, item):
    my_list.insert(0, item) 
    return my_list
print(insert([1, 2, 3], 0))


# 14)

def end(my_list, item):
    my_list.insert(len(my_list), item) 
    return my_list
print(end([1, 2, 3], 4))
