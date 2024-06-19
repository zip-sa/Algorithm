# 3-4.py | 숫자 카드 게임 | 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)