while True:
    x = int(input("x: "))
    y = int(input("y: "))

    if x == y:
        print("Numbers must be different! Try again.")
        continue
    else:
        break

def calculate(x, y):
    if x < y:
        [x, y] = [(x + y) / 2, (x * y) * 2]
    return [x, y]

print(calculate(x, y))