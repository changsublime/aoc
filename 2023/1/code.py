if __name__ == "__main__":
    with open("2023/1/input.txt") as f:
        lines = f.readlines()
        nums = []
        s = 0
        raw = set(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        translate = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

        for l in lines:
            temp = l
            while temp:
                if temp[0] in raw:
                    s += 10 * int(temp[0])
                    break
                for k, i in translate.items():
                    if temp.startswith(k):
                        s += 10 * int(i)
                        temp = ""
                        break
                temp = temp[1:]
            temp = l
            while temp:
                if temp[-1] in raw:
                    s += int(temp[-1])
                    break
                for k, i in translate.items():
                    if temp.endswith(k):
                        s += int(i)
                        temp = ""
                        break
                temp = temp[:-1]

        print(s)