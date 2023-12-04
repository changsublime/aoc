if __name__ == "__main__":
    with open("2023/4/input.txt") as f:
        lines = f.readlines()
    hits = []
    my_nums = []
    p1 = 0

    for line in lines:
        hit, ns = line.split(": ")[1].split("|")
        hits.append(hit.rstrip().split())
        my_nums.append(ns.rstrip().split())

    total = len(hits)
    num_tickets = [1] * total

    for i in range(total):
        cur = 0
        for hit in hits[i]:
            if hit in my_nums[i]:
                cur += 1
                if i + cur < total:
                    num_tickets[i + cur] += num_tickets[i]
        if cur:
            p1 += 2 ** (cur - 1)
    
    print(p1)
    print(sum(num_tickets))