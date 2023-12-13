import numpy as np

if __name__ == "__main__":
    with open("2023/13/input.txt") as f:
        lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    matricies = []
    cur = []
    for line in lines:
        if line:
            cur.append(list(line))
        else:
            matricies.append(cur)
            cur = []
    matricies.append(cur)
    matricies_rotated = [np.rot90(mat, 3).tolist() for mat in matricies]

    def get_num_lines(ms, part=1):
        res = 0
        for mat in ms:
            l = len(mat)
            for i in range(l-1):
                dist_to_edge = i if i < l // 2 else l - i - 2
                p1 = mat[i-dist_to_edge:i+1][::-1]
                p2 = mat[i+1:i+2+dist_to_edge]
                if part == 1:
                    if p1 == p2:
                        res += i + 1
                else:
                    p1_flat = np.array([x for r in p1 for x in r])
                    p2_flat = np.array([x for r in p2 for x in r])
                    if len(np.where(p1_flat != p2_flat)[0]) == 1:
                        res += i + 1
        return res
    
    print(get_num_lines(matricies) * 100 + get_num_lines(matricies_rotated))
    print(get_num_lines(matricies, 2) * 100 + get_num_lines(matricies_rotated, 2))