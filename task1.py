a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def calculate(*args):
    result = []
    for num in args:
        if num >= 0:
            num = num**2
        else:
            num = num**4
        result.append(num)
    return result

print(calculate(a,b,c))