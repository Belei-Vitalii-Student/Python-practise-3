def calc_negative(*numbers):
    count = 0
    for num in numbers:
        if num < 0:
            count = count + 1
    return count

def __main__():
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")

    print(f"Count of negative numbers: {calc_negative(a,b,c)}")

__main__()