from collections import defaultdict

if __name__ == "__main__":
    with open("2023/3/input.txt") as f:
        lines = f.readlines()
        invalid = set(list("1234567890."))
        invalid.add("\n")
        d = defaultdict(list)
        p1, p2 = 0, 0

        for i, line in enumerate(lines):
            head, tail = 0, 1
            while tail <= len(line):
                if line[head].isnumeric() and line[tail].isnumeric() and tail < len(line):
                    tail += 1
                elif line[head].isnumeric():
                    num = int(line[head:min(tail, len(line))])
                    for j in range(max(i-1, 0), min(i+2, len(lines))):
                        for k in range(max(head-1, 0), min(tail+1, len(line))):
                            if lines[j][k] == "*":
                                d[(j, k)].append(num)
                                p1 += num
                            elif lines[j][k] not in invalid:
                                p1 += num
                    head = tail
                    tail = head + 1
                else:
                    head = tail
                    tail = head + 1
        
        for k, v in d.items():
            if len(v) == 2:
                p2 += v[0] * v[1]

        print(p1)
        print(p2)