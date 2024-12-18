while True:
    w, h, char = map(str, input().split())
    print(int(w)*int(h))
    if char == 'C': break