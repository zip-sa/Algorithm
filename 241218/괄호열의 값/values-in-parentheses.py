def calc(b):
    s, t, r = [], 1, 0
    for i, c in enumerate(b):
        if c in '([': t, s = t * (2 if c == '(' else 3), s + [c]
        elif c in ')]' and (not s or abs(ord(c) - ord(s.pop())) > 2): return 0
        else: r, t = r + t if b[i-1] in '([' else r, t // (2 if c == ')' else 3)
    return r if not s else 0

print(calc(input().strip()))
