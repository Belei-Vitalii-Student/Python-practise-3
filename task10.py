def find_divisors(k, *numbers):
    divisors = []
    for num in numbers:
        if num != 0 and k % num == 0:
            divisors.append(num)
    if len(divisors) == 0:
        print(f"k[{k}] is not divisors for numbers!")
    return divisors

def __main__():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    k = int(input("k: "))

    print(f"k[{k}] is divisor for {find_divisors(k,a,b,c)}")

__main__()