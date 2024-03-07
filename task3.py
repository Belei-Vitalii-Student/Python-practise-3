def find_triangle(angle_a, angle_b):
    sum_angles = angle_a + angle_b
    angle_c = 180 - sum_angles

    if sum_angles > 180:
        print("Triangle is not exist.")
    
    if sum_angles == 180 or angle_c == 90:
        if angle_a == 90 or angle_b == 90 or angle_c == 90:
            print("Triangle is 90 degree.")
        else:
            print("Trianlge is exist, but not 90 degree")
    else:
        print("Trianlge is exist, but not 90 degree")
        print(f"Third angle is equal {angle_c} degrees.")
    
angle_a = float(input("Enter first angle (degrees): "))
angle_b = float(input("Enter second angle (degrees): "))

find_triangle(angle_a, angle_b)
