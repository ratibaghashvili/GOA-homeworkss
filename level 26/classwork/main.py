# 1)

def greet(name):
    print(f"გამარჯობა, {name}")

greet("rati")

# 2)

def manual_range(start, end, step):
    range1 = range(start, end, step)

    for i in range1:
        if i %2 == 0: print(i)

manual_range(2, 20, 2)
manual_range(20, 120, 5)
manual_range(1, 21, 6)
manual_range(24, 270, 21)
manual_range(20, 200, 10)

# 3)

def manual_len(list):
    i = 0
    for item in list:
        i += 1  
    print(i)


manual_len([1, 2, 3, 4, 5])
manual_len(["a", "b", "c", "d", "e", "f"])
manual_len([10, 20, 30])
manual_len([1])
manual_len([])