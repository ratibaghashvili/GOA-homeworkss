# 1)

# while-გამოიყენება როცა არ ვიცით რამდენჯერ უნდა გავაკეთოთ რაღაც
# for-გამოიყენება მაშინ როცა ვიცით რამდენჯერ უნდა გავაკეთოთ რაღაც

# 2)

#while

i = 0
while i < 50:
    print("GOA BEST!!!")
    i += 1

# for

for i in range(50):
    print("GOA BEST!!!")


# 3) 
i = 1
while i <= 10:
    print(i)
    i += 1


# 4)
i = 2
while i <= 20:
    print(i)
    i += 2

# 5)

i = 10
while i > 0:
    print(i)
    i -= 1
print("Blast off!")

# 6)

password = "raatiiiiibatiii"
password_entered = input("Enter password: ")
while password_entered != password:
    password_entered = input("Incorrect password Try again: ")
print("Password accepted")

# 7)

correct_username = "kaikaci"
correct_pass = "kaikaci123"
username = input("Enter username: ")
password = input("Enter password: ")
while username != correct_username or password != correct_pass:
    print("Incorrect username or password")
    username = input("Enter username: ")
    password = input("Enter password: ")
print("Login entered")
