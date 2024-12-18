age = []

while True:
    n = int(input())
    if 20 <= n < 30: 
        age.append(n)
        continue
    else: break

print(f"{sum(age)/len(age):.2f}")
