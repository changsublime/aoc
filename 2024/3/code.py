import re

if __name__ == "__main__":
    with open("2024/3/input.txt") as f:
        lines = f.readlines()
    p2 = 0

    total_lines = ""
    for line in lines:
        total_lines += line

    lines_with_dont = total_lines.split("do()")
    for line_with_dont in lines_with_dont:
        line_to_do = line_with_dont.split("don't()")[0]
        muls = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)", line_to_do)
        for mul in muls:
            nums = "".join(mul[4:-1])
            l, r = nums.split(",")
            p2 += int(l) * int(r)

    print(p2)