while True:
    try:
        a, b = map(int, input().split())
        if 1 <= a <= b <= 100:
            break
        else:
            print("범위 오류. 1 ≤ a ≤ b ≤ 100")
    except ValueError:
        exit()
    except EOFError:
        pass

val_sum = 0

start = (a + 5) // 6 * 6

# 6의 배수만 순회
for num in range(start, b + 1, 6):
    if num % 8 != 0:  # 8의 배수가 아닌지 확인
        val_sum += num

print(val_sum)
