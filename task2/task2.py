import math
import sys

def parse_file(file_name):
    with open(file_name, 'r') as file:
        return [list(map(float, line.strip().split()))
                 for line in file.readlines()]
    
def point_in_circle_check(circle, points):
    r_circle = circle[1][0]
    x_point = points[n][0]
    y_point = points[n][1]

    # Normalization of coordinates:
    x_point -= circle[0][0]
    y_point -= circle[0][1]

    hypotenuse = math.sqrt(x_point ** 2 + y_point ** 2)

    if hypotenuse < r_circle:
        return("1")
    elif abs(hypotenuse - r_circle) < 1e-4:
        return("0")
    else:
        return("2")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("How to use: python3 task2.py <file_with_circle> <file_with_points>")
        sys.exit(1)

    circle = parse_file(sys.argv[1])
    points = parse_file(sys.argv[2])
    n = 0
    while n < len(points):
        print(point_in_circle_check(circle, points))
        n += 1

    






