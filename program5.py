# Two-dimentional list 
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for row {i} and column {j}: "))
        row.append(element)
    matrix.append(row)

print("Matrix is here ->")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
         