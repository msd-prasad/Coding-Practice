import math


def grazing_area(R, r, theta):
    theta_rad = (math.pi * theta) / 180.0
    b = 0.5
    sector_area = 0.5 * r * r * theta_rad
    triangle_area = 0.5 * r * (R - r * math.cos(theta_rad))
    grazing_area = sector_area - triangle_area
    if grazing_area > (math.pi * R * b):
        grazing_area = math.pi * R * b
    return grazing_area


R = float(input())
r = float(input())
theta = float(input())
area = grazing_area(R, r, theta)
print(round(area, 3))
