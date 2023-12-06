from collections import deque

if __name__ == "__main__":
    with open("2023/5/input.txt") as f:
        lines = f.readlines()
    
    lines = [l.rstrip() for l in lines]
    
    parsed = [[]]
    for l in lines:
        if not l:
            parsed.append([])
        else:
            parsed[-1].append(l)

    seeds = [[int(i), int(i) + 1] for i in parsed[0][0].split()[1:]]
    seedsp2 = []
    for i in range(len(seeds)):
        if i & 1:
            continue
        else:
            seedsp2.append([seeds[i][0], seeds[i][0] + seeds[i+1][0]])
    
    parsed = [p[1:] for p in parsed]

    def evaluate(seeds):
        res = float("inf")
        to_check = deque(seeds)

        for p in parsed[1:]:
            nextqueue = deque()
            while to_check:
                cur = to_check.popleft()
                hit = False
                for l in p:
                    dest, src, rng = [int(i) for i in l.split()]
                    if src <= cur[0] < src + rng:
                        hit = True
                        diff = cur[0] - src
                        if cur[1] <= src + rng:
                            between = cur[1] - cur[0]
                            nextqueue.append([dest + diff, dest + diff + between])
                            break
                        else:
                            nextqueue.append([dest + diff, dest + rng])
                            to_check.append([src + rng, cur[1]])
                            break

                if not hit:
                    nextqueue.append(cur)
            to_check = nextqueue

        return min([i[0] for i in to_check])

    p1 = evaluate(seeds)
    p2 = evaluate(seedsp2)
    print(p1, p2)