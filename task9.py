def calc_integer(*numbers):
    count = 0
    for num in numbers:
        if num.is_integer():
            count = count + 1
    return count

def __main__():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    print(f"Count of integer numbers: {calc_integer(a,b,c)}")

__main__()