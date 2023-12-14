import itertools

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
        res = 0
        for line in lines:
            c = 0
            memo = set()
            record = line[0]
            l = len(record)
            nums = list(map(int, line[1].split(",")))
            dots = l - sum(nums)
            # pick len(nums) spots to place nums into dots + 1 spots
            ways = list(itertools.combinations(range(dots + 1), len(nums)))
            ways = set([way + (dots,) for way in ways])
            while ways:
                correct = True
                way = ways.pop()
                cur = "." * (way[0] - 0)
                for i in range(len(way)-1):
                    cur += "#" * nums[i] + "." * (way[i+1] - way[i])
                if not cur.startswith(tuple(memo)):
                    for j in range(l):
                        if record[j] == "?":
                            continue
                        elif record[j] != cur[j]:
                            correct = False
                            memo.add(str(cur[:j+1]))
                            break
                else:
                    correct= False
                if correct:
                    c += 1
            res += c
            print(c)
        return str(res)

    print("res: " + evaluate(lines))
    print("p2res: " + evaluate(lines, 2))