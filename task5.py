def new_point(name):
    x = float(input(f"Enter x for {name}: "))
    y = float(input(f"Enter y for {name}: "))

    return [x, y]

def find_place(point):
    x, y = point

    if x == 0 and y == 0:
        print("Point is in center [0,0]")
    elif x == 0 and y != 0:
        print("Point is on y line")
    elif x != 0 and y == 0:
        print("Point is on x line")
    elif x < 0 and y > 0:
        print("Point is in top left side (second quadrant)")
    elif x < 0 and y < 0:
        print("Point is in bottom left side (third quadrant)")
    elif x > 0 and y < 0:
        print("Point is in bottom right side (fourth quadrant)")
    elif x > 0 and y > 0:
        print("Point is in top right side (first quadrant)")

def __main__():
    point = new_point("A")
    find_place(point)

__main__()