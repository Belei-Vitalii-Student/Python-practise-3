def check():
    a = int(input("a: "))
    b = int(input("b: "))

    if a == b:
        a = b = 0
    else:
        if a > b:
            b = a
        else:
            a = b
    return[a, b]

def __main__():
    print(check())

__main__()