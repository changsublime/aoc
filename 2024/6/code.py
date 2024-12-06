from collections import defaultdict
import copy


def check(lines, pos):
    ans = 1
    seen = defaultdict(set)
    while True:
        match char := lines[pos[0]][pos[1]]:
            case "^":
                new_pos = [pos[0] - 1, pos[1]]  # up 1
                if new_pos[0] < 0:  # out of map
                    break
            case "v":
                new_pos = [pos[0] + 1, pos[1]]  # down 1
                if new_pos[0] >= len(lines):  # out of map
                    break
            case ">":
                new_pos = [pos[0], pos[1] + 1]  # right 1
                if new_pos[1] >= len(lines[0]):  # out of map
                    break
            case "<":
                new_pos = [pos[0], pos[1] - 1]  # left 1
                if new_pos[1] < 0:  # out of map
                    break

        if char in seen[(pos[0], pos[1])]:
            return -1  # there is a loop
        
        seen[(pos[0], pos[1])].add(char)

        if lines[new_pos[0]][new_pos[1]] == "#":  # blocked
            match char:
                case "^":
                    lines[pos[0]][pos[1]] = ">"
                case "v":
                    lines[pos[0]][pos[1]] = "<"
                case ">":
                    lines[pos[0]][pos[1]] = "v"
                case "<":
                    lines[pos[0]][pos[1]] = "^"
        else:  # we can go
            lines[pos[0]][pos[1]] = "X"
            if lines[new_pos[0]][new_pos[1]] == ".":
                ans += 1
            lines[new_pos[0]][new_pos[1]] = char
            pos = new_pos
    
    return ans


if __name__ == "__main__":
    with open("2024/6/input.txt") as f:
        lines = [list(l.rstrip()) for l in f.readlines()]
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "^":
                pos = [i,j]
                break
    
    p1 = check(copy.deepcopy(lines), pos)
    print(p1)

    p2 = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if pos[0] == i and pos[1] == j:
                continue
            copied_lines = copy.deepcopy(lines)
            copied_lines[i][j] = "#"
            if check(copied_lines, pos) == -1:
                p2 += 1
    print(p2)

