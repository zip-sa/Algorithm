a, b, c = map(int, input().split())

if a < b and a < c: print(1, end=" ")
else: print(0, end=" ")

if a == b and b == c: print(1, end=" ")
else: print(0, end=" ")

# print(f"{1 if a < b and a < c else 0} {1 if a == b == c else 0}")