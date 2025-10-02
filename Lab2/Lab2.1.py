from math import sqrt

def triangle(side):
    return sqrt(3) / 4 * side ** 2, 3 * side

print(triangle(10))
