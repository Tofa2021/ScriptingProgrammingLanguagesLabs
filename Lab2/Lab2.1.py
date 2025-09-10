from math import sqrt

def triangle(side):
    triangle_square = sqrt(3) / 4 * side ** 2
    triangle_perimeter = 3 * side
    return triangle_square, triangle_perimeter

square, perimeter = triangle(10)
print(square)
print(perimeter)