if __name__ == "__main__":
    with open("2023/2/input.txt") as f:
        lines = f.readlines()
        games = [l.split(": ")[1].split("; ") for l in lines]
        res = 0

        for i, g in enumerate(games):
            bag = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for s in g:
                element = s.split(", ")
                for e in element:
                    n, color = e.split()
                    bag[color] = max(bag[color], int(n))
            res += bag["red"] * bag["green"] * bag["blue"]
        
        print(res)
