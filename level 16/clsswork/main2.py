my_num = 7  
counter = 0  
while True:
    guess = int(input("გამოიცანით რიცხვი 1-დან 10-მდე: "))
    counter = 0
    if guess == my_num:
        print(counter)
        break  
