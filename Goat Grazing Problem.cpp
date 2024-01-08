#include <iostream>
#include <cmath>
double grazing_area(double R, double r, double theta) {
double theta_rad = M_PI * theta / 180.0;
double b = 1.0 / 2.0;
double sector_area = 0.5 * r * r * theta_rad;
double triangle_area = 0.5 * r * (R - r * cos(theta_rad));
double grazing_area = sector_area - triangle_area;
if (grazing_area > M_PI * R * b) {
grazing_area = M_PI * R * b;
}
return round(grazing_area * 1000.0) / 1000.0;
}
int main() {
double R, r, theta;
std::cin >> R >> r >> theta;
double area = grazing_area(R, r, theta);
std::cout << area << std::endl;
return 0;
}

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
print(area.round(3))
