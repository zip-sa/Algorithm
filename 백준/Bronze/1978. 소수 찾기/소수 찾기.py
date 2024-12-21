def solution():
    N = int(input())
    numbers = list(map(int, input().split()))

    max_num = max(numbers) if numbers else 0
    sieve = [True] * (max_num + 1)
    sieve[0], sieve[1] = False, False

    for i in range(2, int(max_num**0.5) + 1):
        for j in range(i * i, max_num + 1, i):
            sieve[j] = False
    prime_count= sum(1 for num in numbers if sieve[num])

    print(prime_count)

solution()
