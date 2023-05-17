x = 10  # global variable:


def func1():
    global x
    x = x+5
    print(x)


func1()

# and modifying the global x = 10+5 = 15;
print(x)
