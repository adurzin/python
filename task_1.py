class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                self.my_list[i][j] = self.my_list[i][j] + other.my_list[i][j]
        return Matrix(self.my_list)

    def __str__(self):
        return "{}\n".format("\n".join(map(str, ([" ".join(map(str, self.my_list[i]))
                                                  for i in range(len(self.my_list))]))))


matrix_1 = Matrix([[12, 22, 32], [11, 52, 23]])
matrix_2 = Matrix([[12, 25, 33], [65, 21, 35]])
matrix_3 = Matrix([[1, 1, 1], [1, 1, 1]])
print(matrix_1)
print(matrix_1 + matrix_2)
print(matrix_1)
print(matrix_1 + matrix_3)
