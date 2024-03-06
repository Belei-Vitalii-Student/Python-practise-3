import math

def new_point(name):
    x = int(input(f"Enter x for {name}: "))
    y = int(input(f"Enter y for {name}: "))

    return {
        "name": name,
        "coords": [x, y]
    }

point_a = new_point("A")
point_b = new_point("B")

def find_closest(point_a, point_b):
    distance_a = math.sqrt(point_a["coords"][0]**2 + point_a["coords"][1]**2)
    distance_b = math.sqrt(point_b["coords"][0]**2 + point_b["coords"][1]**2)
    
    if distance_a < distance_b:
        return point_a["name"]
    elif distance_a > distance_b:
        return point_b["name"]

print(f"Closest point is: {find_closest(point_a, point_b)}")


