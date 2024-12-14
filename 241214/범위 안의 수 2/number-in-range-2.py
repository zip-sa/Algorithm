def calculate_sum_and_average():
    arr = []

    for _ in range(10):
        while True:
            try:
                num = int(input())
                if -500 <= num <= 500:
                    arr.append(num)
                    break
            except ValueError:
                pass

    valid_numbers = [num for num in arr if 0 <= num <= 200]

    total = sum(valid_numbers)
    average = round(total / len(valid_numbers), 1)

    print(total, average)

calculate_sum_and_average()
