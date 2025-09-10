from mpmath import swap_row

print("Введите n")
n = int(input())
print("Введите m")
m = int(input())

print("Введите значения матрицы")
matrix = [[input() for _ in range(n)] for _ in range(m)]
print(matrix)

print("Введите i")
i = int(input())
print("Введите j")
j = int(input())

swap_row(matrix, i, j)
print(matrix)