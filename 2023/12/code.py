import re

def main():
    with open("2023/12/input.txt") as f:
        lines = f.readlines()
#     lines = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1""".split("\n")
#     print(lines)
    lines = [line.rstrip().split() for line in lines]
    # lines = [['?????#?#?', '1,1,3']]

    def evaluate(lines, folds=1):
        lines = [
            [
                "".join(list((line[0] + "?") * folds)[:-1]), 
                "".join(list((line[1] + ",") * folds)[:-1])
            ] 
            for line in lines
        ]

        def build_possibilities(cur, remainder, check, memo):
            if not remainder:
                return cur
            step = []
            for c in cur:
                full = [len(s) for s in re.split(r'\.+', c) if s]
                comp = tuple(full[:-1])
                if comp in memo:
                    continue
                elif len(full) > len(check):
                    continue
                elif comp and comp != tuple(check[:len(comp)]):
                    memo.add(comp)
                    continue
                elif remainder[0] == "?":
                    step.append(c + ".")
                    step.append(c + "#")
                else:
                    step.append(c + remainder[0])
            return build_possibilities(step, remainder[1:], check, memo)

        res = []
        for line in lines:
            c = 0
            memo = set()
            arrs = [int(j) for j in line[1].split(",")]
            possibilities = build_possibilities([""], line[0], arrs, memo)
            for p in possibilities:
                comp = [len(s) for s in re.split(r'\.+', p) if s]
                if comp == arrs:
                    c += 1
            if c:
                res.append(c)
                #print(c)
        return res

    p1_list = evaluate(lines)
    print(sum(p1_list))

    # step = 50
    # for i in range(0, len(lines), 50):
    #     print(evaluate(lines[i:i+50], 5))

    # p2 = 0
    # patterns = list(zip(p1_list, evaluate(lines, 2)))
    # for i, pattern in enumerate(patterns):
    #     m, r = divmod(pattern[1], pattern[0])
    #     if r:
    #         print(i, p2)
    #         p2 += evaluate([lines[i]], 5)[0]
    #     else:
    #         p2 += pattern[1] * (m ** 3)
    # print(p2)


if __name__ == "__main__":
    main()