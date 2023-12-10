from collections import deque


def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                return [i, j]

if __name__ == "__main__":
    with open("2023/10/input.txt") as f:
        lines = f.readlines()
    matrix = [list(l.rstrip()) for l in lines]
    start = find_start(matrix)

    cur = [start[0] + 1, start[1]]
    direction = "down"
    path_length = 1
    visited = set([tuple(start)])

    # holds every point to the left of the loop
    # going clockwise
    starts = set()

    while cur != start:
        visited.add(tuple(cur))
        match matrix[cur[0]][cur[1]]:
            case "|":
                if direction == "down":
                    starts.add((cur[0], cur[1]+1))
                    cur[0] += 1
                else:
                    starts.add((cur[0], cur[1]-1))
                    cur[0] -= 1
            case "-":
                if direction == "right":
                    starts.add((cur[0]-1, cur[1]))
                    cur[1] += 1
                else:
                    starts.add((cur[0]+1, cur[1]))
                    cur[1] -= 1
            case "L":
                if direction == "left":
                    starts.add((cur[0], cur[1]-1))
                    starts.add((cur[0]+1, cur[1]-1))
                    starts.add((cur[0]+1, cur[1]))
                    cur[0] -= 1
                    direction = "up"
                else:
                    cur[1] += 1
                    direction = "right"
            case "J":
                if direction == "down":
                    starts.add((cur[0], cur[1]+1))
                    starts.add((cur[0]+1, cur[1]+1))
                    starts.add((cur[0]+1, cur[1]))
                    cur[1] -= 1
                    direction = "left"
                else:
                    cur[0] -= 1
                    direction = "up"
            case "7":
                if direction == "right":
                    starts.add((cur[0], cur[1]+1))
                    starts.add((cur[0]-1, cur[1]+1))
                    starts.add((cur[0]-1, cur[1]))
                    cur[0] += 1
                    direction = "down"
                else:
                    cur[1] -= 1
                    direction = "left"
            case "F":
                if direction == "left":
                    cur[0] += 1
                    direction = "down"
                else:
                    starts.add((cur[0], cur[1]-1))
                    starts.add((cur[0]-1, cur[1]-1))
                    starts.add((cur[0]-1, cur[1]))
                    cur[1] += 1
                    direction = "right"
        path_length += 1
    
    n = len(matrix)
    m = len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    starts -= visited

    while starts:
        start = starts.pop()
        if start not in visited:
            queue = deque([start])
            while queue:
                nextqueue = deque()
                cur = queue.popleft()
                visited.add(cur)
                x, y = cur
                for dx, dy in directions:
                    if 0 <= x + dx < len(matrix) and 0 <= y + dy < len(matrix[0]):
                        if (x + dx, y + dy) not in visited:
                            nextqueue.append((x + dx, y + dy))
                queue = nextqueue

    print(path_length // 2)
    print(len(visited) - path_length)