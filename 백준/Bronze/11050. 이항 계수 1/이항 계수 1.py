def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def solution(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n, k = map(int, input().split())

print(solution(n, k))
