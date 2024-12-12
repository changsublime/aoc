memo = {"0": "1"}
ans_memo = {}

def blink(ns, i):
    if ns in ans_memo.keys() and ans_memo[ns][i] != -1:
        return ans_memo[ns][i]
    
    nums = ns.split()

    if i == 0:
        return len(nums)
    
    ans = 0
    for n in nums:
        memoed = -1
        if n in memo.keys():
            memoed = blink(memo[n], i-1)
        elif len(n) % 2 == 0:
            prefix = str(int(n[0:len(n)//2]))
            suffix = str(int(n[len(n)//2:]))
            memoed = blink(prefix, i-1) + blink(suffix, i-1)
            memo[n] = prefix + " " + suffix
        else:
            mult = str(int(n) * 2024)
            memoed = blink(mult, i-1)
            memo[n] = mult
        
        ans += memoed

        if n not in ans_memo.keys():
            ans_memo[n] = [-1] * 76
        if ans_memo[n][i] == -1:
            ans_memo[n][i] = memoed

    return ans


if __name__ == "__main__":
    with open("2024/11/input.txt") as f:
        nums = [l.rstrip() for l in f.readlines()][0]

    ans = blink(nums, 75)
    print(ans)
    