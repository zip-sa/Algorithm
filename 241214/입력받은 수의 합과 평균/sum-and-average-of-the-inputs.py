numbers = []

while True:
    try:
        n = int(input())
        if 1 <= n <= 100:
            break
        else:
            print("n은 1 이상 100 이하의 자연수여야 합니다.")
    except ValueError:
        print("유효한 정수를 입력하세요.")

for _ in range(n):
    while True:
        try:
            num = int(input())
            if 1 <= num <= 1000:
                numbers.append(num)
                break
            else:
                print("숫자는 1 이상 1,000 이하만 입력 가능합니다.")
        except ValueError:
            print("유효한 정수를 입력하세요.")
        except EOFError:
            print("입력이 중단되었습니다.")
            exit()

num_sum = sum(numbers)
num_avg = round(num_sum / len(numbers), 1)

print(num_sum, num_avg)
