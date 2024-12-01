from collections import defaultdict


if __name__ == "__main__":
    with open("2024/1/input.txt") as f:
        lines = f.readlines()

    l, r = [], []
    for line in lines:
        s = line.rstrip().split()
        l.append(int(s[0]))
        r.append(int(s[1]))
    l.sort()
    r.sort()

    p1 = 0
    for i in range(len(l)):
        p1 += abs(l[i] - r[i])

    p2 = 0
    r_map = defaultdict(int)
    for n in r:
        r_map[n] += 1

    for n in l:
        p2 += n * r_map[n]

    print(p1)
    print(p2)
