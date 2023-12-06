if __name__ == "__main__":
    with open("2023/6/input.txt") as f:
        lines = f.readlines()

    times = [int(i) for i in lines[0].rstrip().split()[1:]]
    distances = [int(i) for i in lines[1].rstrip().split()[1:]]
    times.append(int(lines[0].split(":")[1].replace(" ", "")))
    distances.append(int(lines[1].split(":")[1].replace(" ", "")))

    res = []
    p1 = 1

    for i in range(len(times)):
        low, high = 0, times[i]
        while low < high:
            mid = (low + high) // 2
            if mid * (times[i] - mid) > distances[i]:
                high = mid
            else:
                low = mid + 1
        res.append(times[i] - 2 * low + 1)

    for i in res[:-1]:
        p1 *= i

    print(p1, res[-1])