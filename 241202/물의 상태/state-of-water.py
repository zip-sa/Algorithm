n = int(input())

if n >= 100: print("vapor")
elif n < 0: print("ice")
else:
    print("water")

# print("ice" if n < 0 else "vapor" if n >= 100 else "water")