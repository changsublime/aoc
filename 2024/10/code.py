def find_score(trail, position):
    x, y = position
    ans = 0
    score = int(trail[x][y])

    if trail[x][y] == '9':
        return 1
    
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if i < 0 or j < 0 or i >= len(trail) or j >= len(trail[0]):
            continue
        elif trail[i][j] == str(score + 1):
            ans += find_score(trail, (i, j))
    
    return ans


if __name__ == "__main__":
    with open("2024/10/input.txt") as f:
        lines = [list(l.rstrip()) for l in f.readlines()]
    
    p2 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '0':
                p2 += find_score(lines, (i, j))
    
    print(p2)
    