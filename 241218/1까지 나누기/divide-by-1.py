n = int(input())

for i in range(1, n+1):
    n //= i
    if n // i == 0: 
        print(i+1)
        break
