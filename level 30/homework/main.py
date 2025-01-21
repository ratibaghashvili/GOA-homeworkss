# 1)

goa = "goa is best academy"
print(goa.upper())

# 2)

name = input("Enter your name: ")
print(name.upper())

# 3)

def uppercase(list):
    return [item.upper() for item in list]
string = ['goa', 'is', 'best']
print(uppercase(string))

# 4)

academy = "GOA IS BEST"
print(academy.lower())


# 5)

email = input("Enter your email address: ")
print(email.lower())


# 6)

def lowercase(string):
    return string.lower()

print(lowercase("GoA bEsT"))

 
# 7) 

capital = input("Enter a text: ")
print(capital.capitalize())



# 8)


string = ['goa', 'is', 'fire']
capital = [i.capitalize() for i in string]
print(capital)


# 9)

def first(string):
    return string.capitalize()
print(first("gaumarjos"))


# 10)

raviaba = "goa is best academy in world , Goa is best"
pos = raviaba.find("academy")
print(pos)


# 11)

str = input("enter a string: ")
sub = input("enter the substring to search for: ")
pos = str.find(sub)
print(pos)


# 12)

def char1(string, char):
    return string.find(char)

print(char1("goaa", 'e'))


# 13)

enter = input("enter a string: ")
print("length of the string is:", len(enter))


# 14)

def lengths(string):
    return [len(i) for i in string]
string = ['goa', 'is', 'best']
print(lengths(string))

# 15)

para = "The quick brown fox jumps over the lazy dog. The dog didn't move."
count = para.lower().split().count("the")
print("The word 'the' appears", count, "times.")

# 16)

string = input("Enter a string: ")
char = input("Enter a character to count its occurrences: ")
count = string.count(char)
print(char , count )


# 17)

def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())
text = input("Enter a text: ")
word = input("Enter a word to count its occurrences: ")
print(word)

# 18)

text = input("Enter a string: ")
index = text.find("hello")
if index != -1:
    print(index)
else:
    print("The word 'hello' was not found in the string.")


# 19)

def find_character_index(user_string, char):
    return user_string.find(char)

user_string = input("Enter a string: ")
char = input("Enter a character to find its index: ")
index = find_character_index(user_string, char)
if index != -1:
    print(char,index)
else:
    print(char)


# 20)

user_string = input("Enter a string: ")
if user_string.islower():
    print("all characters in the string are lowercase.")
else:
    print("Not all characters in the string are lowercase.")


# 21)

def is_all_lowercase(user_string):
    return user_string.islower()

user_string = input("Enter a string: ")
print(is_all_lowercase(user_string))

# 22)

user_string = input("Enter a string: ")
if user_string.islower():
    print("The string contains only lowercase letters.")
else:
    print("The string does not contain only lowercase letters.")


# 23)

user_string = input("Enter a string: ")
if user_string.isupper():
    print("All characters in the string are uppercase.")
else:
    print("Not all characters in the string are uppercase.")


# 24)

def is_all_uppercase(user_string):
    return user_string.isupper()

user_string = input("Enter a string: ")
print(is_all_uppercase(user_string))


# 25)

user_string = input("Enter a string: ")
if user_string.isupper():
    print("The string is in uppercase.")
else:
    print("The string is not in uppercase.")
