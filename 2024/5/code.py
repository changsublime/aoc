from collections import defaultdict


if __name__ == "__main__":
    with open("2024/5/input.txt") as f:
        lines = f.readlines()
    
    p1, p2 = 0, 0

    rules = []
    pages = []

    break_seen = False

    for line in lines:
        l = line.rstrip()
        if not break_seen and l == "":
            break_seen = True
            continue
        if not break_seen:
            rules.append(l)
        else:
            pages.append(l)

    rules_dict = defaultdict(set)  # number: set of numbers that should be in front of it
    for rule in rules:
        k, v = rule.split("|")
        rules_dict[k].add(v)
    
    def reorder(l):
        s = set(l)
        reordered = []
        while s:
            full_rules = set()
            to_discard = None
            for e in s:
                full_rules |= rules_dict[e]
            for e in s:
                if e not in full_rules:
                    to_discard = e
            reordered.append(to_discard)
            s.discard(to_discard)
        return int(reordered[(len(reordered)-1)//2])
    
    for page in pages:
        p = page.split(",")
        good = True
        for i, n in enumerate(p):
            for prefix in p[:i]:
                if prefix in rules_dict[n]:
                    good = False
        if good:
            p1 += int(p[(len(p)-1)//2])
        else:
            p2 += reorder(p)

    print(p1)
    print(p2)