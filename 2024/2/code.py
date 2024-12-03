def check_broken(l: list) -> bool:
    broken = False
    for i, e in enumerate(l[:-1]):
        if not (1 <= l[i+1] - e <= 3):
            broken = True
    return broken

# p2
def check_broken_subsets(l: list) -> bool:
    if not check_broken(l):
        return False
    
    for i in range(len(l)):
        sublist = l[:i] + l[i+1:]
        broken = check_broken(sublist)
        if not broken:
            return broken
    return True
    

if __name__ == "__main__":
    with open("2024/2/input.txt") as f:
        lines = f.readlines()
    
    ans = 0
    
    for line in lines:
        l = [int(i) for i in line.split()]
        if not check_broken_subsets(l):
            ans += 1
        elif not check_broken_subsets(list(reversed(l))):
            ans += 1
        else:
            continue
        
    print(ans)