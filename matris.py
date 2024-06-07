def get_matrix_from_user():
    rows = int(input("enter the amount of rows "))
    cols = int(input("enter the amount of columns "))

    matrix = []
    print("enter the elemens of matrix ")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"element [{i+1},{j+1}]: "))
            row.append(element)
        matrix.append(row)

    L_rows = len(matrix)
    L_cols = len(matrix[0])
    if L_rows != L_cols:
        print( "the rows and columns is not balance")
    diagonal_sum = 0
    for i in range(rows):
        diagonal_sum += matrix[i][i]
    print( diagonal_sum)






get_matrix_from_user()


