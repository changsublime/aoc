def determine(ans, nums, p2):
    if len(nums) == 1:
        return ans == nums[0]
    x = nums.pop(-1)
    out = determine(ans - x, nums[:], p2)

    div = ans / x
    if div.is_integer():
        out += determine(int(div), nums[:], p2)

    if p2 and x >= 0 and str(ans).endswith(str(x)):
        head = ans // (10 ** len(str(x)))
        out += determine(head, nums[:], p2)
    return out


if __name__ == "__main__":
    with open("2024/7/input.txt") as f:
        lines = [l.rstrip() for l in f.readlines()]
    
    p1, p2 = 0, 0

    for line in lines:
        ans, eq = line.split(":")
        ans = int(ans)
        nums = [int(n) for n in eq.split()]
        if determine(ans, nums[:], False):
            p1 += ans
        if determine(ans, nums[:], True):
            p2 += ans
    
    print(p1)
    print(p2)