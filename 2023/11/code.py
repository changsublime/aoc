if __name__ == "__main__":
    with open("2023/11/input.txt") as f:
        lines = f.readlines()
    matrix = [list(l.rstrip()) for l in lines]
    m = len(matrix)
    n = len(matrix[0])
    galaxies = []

    doublerows = set(range(m))
    doublecols = set(range(n))

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "#":
                galaxies.append((i, j))
                doublerows.discard(i)
                doublecols.discard(j)
    
    doublerows = sorted(list(doublerows))
    doublecols = sorted(list(doublecols))

    def evaluate(age=2):
        age -= 1
        res = 0
        for i in range(len(galaxies)-1):
            r1, c1 = galaxies[i]
            for j in range(i+1, len(galaxies)):
                r2, c2 = galaxies[j]
                res += abs(r2 - r1) + abs(c2 - c1)
                for row in doublerows:
                    if r1 < row < r2 or r2 < row < r1:
                        res += age
                for col in doublecols:
                    if c1 < col < c2 or c2 < col < c1:
                        res += age
        return res
    
    print(evaluate())
    print(evaluate(1_000_000))