from collections import defaultdict

if __name__ == "__main__":
    with open("2023/7/input.txt") as f:
        lines = f.readlines()
    lines = [l.strip().split() for l in lines]

    def evaluate(lines=lines, part=1):
        replace = {
            "A": "a", 
            "K": "b",
            "Q": "c",
            "J": "d",
            "T": "e",
            "9": "f",
            "8": "g",
            "7": "h",
            "6": "i",
            "5": "j",
            "4": "k",
            "3": "l",
            "2": "m",
            "1": "n",
        }

        if part == 2:
            replace["J"] = "o"

        for k, v in replace.items():
            lines = [[l[0].replace(k, v), int(l[1])] for l in lines]
        
        hands = [[], [], [], [], [], [], []]

        for line in lines:
            d = defaultdict(int)
            for c in line[0]:
                d[c] += 1
            if "o" in d.keys():
                jokers = d["o"]
                if jokers != 5:
                    d.pop("o")
                    max_points = max(d, key=d.get)
                    d[max_points] += jokers
            values = d.values()
            if 5 in values:
                hands[6].append(line)
            elif 4 in values:
                hands[5].append(line)
            elif 3 in values and 2 in values:
                hands[4].append(line)
            elif 3 in values:
                hands[3].append(line)
            elif sorted(list(values)) == [1, 2, 2]:
                hands[2].append(line)
            elif 2 in values:
                hands[1].append(line)
            else:
                hands[0].append(line)
        
        hands = [sorted(h)[::-1] for h in hands]
        hands = [i for h in hands for i in h]

        res = 0
        for i, h in enumerate(hands):
            res += h[1] * (i + 1)
            
        return res

    print(evaluate())
    print(evaluate(part=2))
