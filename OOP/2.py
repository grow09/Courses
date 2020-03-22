class Matrix(object):
    def Matrix(self, a):
        self.a = a
        self.columns = len(a[0])
        self.rows = len(a)

    def addition(self, b):
        i = 0
        j = 0
        for i in range(self.rows - 1):
            for j in range(self.columns):
                self.a[i][j] = self.a[i][j] + b[i][j]
            i = i+1
            for j in range(self.columns):
                self.a[i][j] = self.a[i][j] + b[i][j]
        return "сложеная матрица %s" % self.a

    def multiplication(self, x):
        i = 0
        j = 0
        for i in range(self.rows - 1):
            for j in range(self.columns):
                self.a[i][j] = self.a[i][j] * x
            i = i+1
            for j in range(self.columns):
                self.a[i][j] = self.a[i][j] * x
        return "матрица умноженая на " + str(x) + " %s" % self.a

    def print_(self, a):
        # сложение
        p1 = Matrix()
        p1.Matrix(a)
        print(p1.addition(b = [[3, 4, 1],[4, 3, 2]]))
        # умножение
        p2 = Matrix()
        p2.Matrix(a)
        print(p2.multiplication(x = 2))
        for row in a: 
            for x in row: 
                print ( "{:4d}".format(x), end = "" ) 
            print ()

if __name__ == "__main__":
    p3 = Matrix()
    p3.print_(a = [[1, 2, 3],[4, 5, 6]])
    # # сложение
    # p1 = Matrix()
    # p1.Matrix(a = [[1, 2, 3],[4, 5, 6]])
    # print(p1.addition(b = [[3, 4, 1],[4, 3, 2]]))
    # # умножение
    # p2 = Matrix()
    # p2.Matrix(a = [[1, 2, 3],[4, 5, 6]])
    # print(p2.multiplication(x = 2))

