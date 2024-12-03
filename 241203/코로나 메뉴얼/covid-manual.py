P1_x, P1_y = map(str, input().split())
P2_x, P2_y = map(str, input().split())
P3_x, P3_y = map(str, input().split())

count = 0

if count == 0:
    if P1_x == 'Y' and int(P1_y) >= 37: count += 1
    if P2_x == 'Y' and int(P2_y) >= 37: count += 1
    if P3_x == 'Y' and int(P3_y) >= 37: count += 1

if count >= 2:
    print("E")
else:
    print("N")