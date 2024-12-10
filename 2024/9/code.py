import time
from typing_extensions import Self


class Node:
    def __init__(self, prev, next, val, freq):
        self.prev: Self | None = prev
        self.next: Self | None = next
        self.val: str = val
        self.freq: int = freq


def p1(blocks, num_chars):
    updated_blocks = ["."] * len(blocks)
    head = 0
    tail = -1
    i = 0
    checksum = 0
    while i < num_chars:
        if blocks[head] != ".":
            updated_blocks[i] = blocks[head]
            checksum += i * int(updated_blocks[i])
            head += 1
            i += 1
        elif blocks[tail] != ".":
            updated_blocks[i] = blocks[tail]
            checksum += i * int(updated_blocks[i])
            tail -= 1
            head += 1
            i += 1
        else:
            tail -= 1
    return checksum

def p2(head, tail):
    while head != tail:
        if tail.val == '.':
            pass
        else:
            val, freq = tail.val, tail.freq
            cur = head
            while cur and cur != tail:
                if cur.val == '.' and int(cur.freq) >= int(freq):
                    cur.next = Node(
                        prev = cur,
                        next = cur.next,
                        val = '.',
                        freq = str(int(cur.freq) - int(freq))
                    )
                    cur.val = val
                    cur.freq = freq
                    tail.val = '.'
                    break
                else:
                    cur = cur.next
            cur = head
            b = []
        tail = tail.prev
    
    cur = head
    b = []
    while cur:
        b.extend([cur.val] * int(cur.freq))
        cur = cur.next
    return sum([i * int(n) for i, n in enumerate(b) if n != '.'])


if __name__ == "__main__":
    with open("2024/9/input.txt") as f:
        lines = [l.rstrip() for l in f.readlines()][0]
    
    blocks = []
    n = 0
    num_chars = 0
    nodes = []
    for num in lines:
        if n % 2 == 0:
            blocks.extend([str(n//2)] * int(num))
            num_chars += int(num)
            nodes.append(
                Node(
                    prev = nodes[-1] if nodes else None,
                    next = None,
                    val = str(n//2),
                    freq = num
                )
            )
        else:
            blocks.extend(["."] * int(num))
            nodes.append(
                Node(
                    prev = nodes[-1] if nodes else None,
                    next = None,
                    val = ".",
                    freq = num
                )
            )

        if len(nodes) >= 2:
            nodes[-2].next = nodes[-1]
        n += 1


    print(p1(blocks, num_chars))
    print(p2(nodes[0], nodes[-1]))