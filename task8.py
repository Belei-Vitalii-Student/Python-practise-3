def calc_positive(*numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count = count + 1
    return count

def __main__():
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    print(f"Count of positive numbers: {calc_positive(a,b,c)}")

__main__()