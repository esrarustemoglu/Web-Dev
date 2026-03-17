a = int(input())

k = 2
while k * k <= a:
    if a % k == 0:
        print(k)
        break
    k += 1
else:
    print(a)