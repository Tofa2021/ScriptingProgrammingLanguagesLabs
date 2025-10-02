def show_matrix(matrix, rows, cols):
    print("Ваш массив:")
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end=' ')
        print()

n = int(input("Введите n:"))
m = int(input("Введите m:"))

print("Введите значения матрицы:")
nums = input().split()
matrix = [[int(input()) for _ in range(n)] for _ in range(m)]
show_matrix(matrix, n, m)

i = int(input("Введите i:")) - 1
j = int(input("Введите j:")) - 1

for row in matrix:
    row[i], row[j] = row[j], row[i]

show_matrix(matrix, n, m)
