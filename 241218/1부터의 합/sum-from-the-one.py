n = int(input())
val_sum = 0

for i in range(n):
    if val_sum+i >= n: break
    val_sum += i
    
print(val_sum)
