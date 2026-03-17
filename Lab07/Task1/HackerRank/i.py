if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    maximum = max(arr)
    second_max = None

    for num in arr:
        if num != maximum:
            if second_max is None or num > second_max:
                second_max = num

    print(second_max)