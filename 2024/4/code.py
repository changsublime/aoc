if __name__ == "__main__":
    with open("2024/4/input.txt") as f:
        lines = f.readlines()

    matrix = []
    for line in lines:
        matrix.append(list(line.rstrip()))

    def check(i, j):
        out = 0
        if not matrix[i][j] == "X":
            return 0
        # right
        if matrix[i][j:j+4] == ["X", "M", "A", "S"]:
            out += 1
        # left
        if matrix[i][j-3:j+1] == ["S", "A", "M", "X"]:
            out += 1
        
        if i-3 >= 0:
            # up
            if (matrix[i-1][j], matrix[i-2][j], matrix[i-3][j]) == ("M", "A", "S"):
                out += 1
            # right up
            if j+3 < len(matrix[0]) and ((matrix[i-1][j+1], matrix[i-2][j+2], matrix[i-3][j+3]) == ("M", "A", "S")):
                out += 1
            # left up
            if j-3 >= 0 and ((matrix[i-1][j-1], matrix[i-2][j-2], matrix[i-3][j-3]) == ("M", "A", "S")):
                out += 1    

        if i+3 < len(matrix):   
            # down
            if (matrix[i+1][j], matrix[i+2][j], matrix[i+3][j]) == ("M", "A", "S"):
                out += 1
            # right down
            if j+3 < len(matrix[0]) and ((matrix[i+1][j+1], matrix[i+2][j+2], matrix[i+3][j+3]) == ("M", "A", "S")):
                out += 1
            # left down
            if j-3 >= 0 and ((matrix[i+1][j-1], matrix[i+2][j-2], matrix[i+3][j-3]) == ("M", "A", "S")):
                out += 1   
        
        return out
            

    def check_mas(i, j):
        if not matrix[i][j] == "A":
            return 0
        if i == 0 or j == 0:
            return 0
        if i == len(matrix)-1 or j == len(matrix[0])-1:
            return 0
        
        # is left top and right bottom mas
        if not (
            (matrix[i-1][j-1] == "M" and matrix[i+1][j+1] == "S")
            or
            (matrix[i-1][j-1] == "S" and matrix[i+1][j+1] == "M")
        ):
            return 0
        
        # is right top and left bottom mas
        if not (
            (matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S")
            or
            (matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M")
        ):
            return 0

        return 1

    p1, p2 = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            p1 += check(i, j)
            p2 += check_mas(i, j)

    print(p1)
    print(p2)