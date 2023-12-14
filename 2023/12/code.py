import re

if __name__ == "__main__":
    with open("2023/12/input.txt") as f:
        lines = f.readlines()
    lines = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")
    print(lines)
    lines = [line.rstrip().split() for line in lines]

    def evaluate(lines, folds=1):
        lines = [
            [
                "".join(list((line[0] + "?") * folds)[:-1]), 
                "".join(list((line[1] + ",") * folds)[:-1])
            ] 
            for line in lines
        ]

        def build_possibilities(cur, remainder, check):
            nonlocal memo
            if not remainder:
                return cur
            step = []
            for c in cur:
                comp = tuple([len(s) for s in re.split(r'\.+', c) if s][:-1])
                if comp in memo:
                    continue
                elif len(comp) > 1 and comp != tuple(check[:len(comp)]):
                    memo.add(comp)
                    continue
                elif remainder[0] == "?":
                    step.append(c + ".")
                    step.append(c + "#")
                else:
                    step.append(c + remainder[0])
            return build_possibilities(step, remainder[1:], check)

        res = 0
        for line in lines:
            c = 0
            memo = set()
            arrs = [int(i) for i in line[1].split(",")]
            possibilities = build_possibilities([""], line[0], arrs)
            for p in possibilities:
                comp = [len(s) for s in re.split(r'\.+', p) if s]
                if comp == arrs:
                    c += 1
            if c:
                #print(c)
                res += c
        return str(res)

    print("res: " + evaluate(lines))
    print("p2res: " + evaluate(lines, 4))