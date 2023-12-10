def predict(nums):
    if not any(nums):
        return 0, 0
    next_nums = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    return (
        nums[0] - predict(next_nums)[0],
        nums[-1] + predict(next_nums)[1]
        )
    

if __name__ == "__main__":
    with open("2023/9/input.txt") as f:
        lines = f.readlines()
    lines = [l.rstrip().split() for l in lines]
    vals = []

    for l in lines:
        cur = [int(v) for v in l]
        vals.append(cur)

    p2, p1 = 0, 0
    for vs in vals: 
        d2, d1 = predict(vs)
        p2 += d2
        p1 += d1
    
    print(p1, p2)