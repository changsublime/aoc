from math import gcd

if __name__ == "__main__":
    with open("2023/8/input.txt") as f:
        lines = f.readlines()
    instruction = lines[0].strip()

    def evaluate(part=1):
        res = 0
        starts = set(["AAA"])
        d = {}
        for l in lines[2:]:
            k, v = l.strip().split(" = ")
            d[k] = v[1:-1].split(", ")
            if k[-1] == "A" and part == 2:
                starts.add(k)

        pos = 0
        out = []

        while starts:
            step = set()
            for cur in starts:
                n = d[cur][0] if instruction[pos] == "L" else d[cur][1]
                if n[-1] == "Z" and part == 2:
                    out.append(res + 1)
                elif n == "ZZZ":
                    out.append(res + 1)
                else:
                    step.add(n)
            starts = step
            pos += 1
            pos %= len(instruction)
            res += 1

        lcm = 1
        for i in out:
            lcm = lcm * i // gcd(lcm, i)
        
        return lcm

    print(evaluate())
    print(evaluate(part=2))