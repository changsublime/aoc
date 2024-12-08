from collections import defaultdict


if __name__ == "__main__":
    with open("2024/8/input.txt") as f:
        lines = [l.rstrip() for l in f.readlines()]
    
    ans = set()

    nodes = defaultdict(list)
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != ".":
                nodes[lines[i][j]].append((i,j))
                ans.add((i,j))
    
    for k, v in nodes.items():
        for i, loc in enumerate(v[:-1]):
            for loc_2 in v[i+1:]:
                diff = (loc_2[0] - loc[0], loc_2[1] - loc[1])

                x = loc_2[0] + diff[0]
                y = loc_2[1] + diff[1]
                while (
                    0 <= x < len(lines)
                    and 0 <= y < len(lines[0])
                ):
                    ans.add((x, y))
                    x += diff[0]
                    y += diff[1]

                x = loc[0] - diff[0]
                y = loc[1] - diff[1]
                while (
                    0 <= x < len(lines)
                    and 0 <= y < len(lines[0])
                ):
                    ans.add((x, y))
                    x -= diff[0]
                    y -= diff[1]
                
    print(len(ans))