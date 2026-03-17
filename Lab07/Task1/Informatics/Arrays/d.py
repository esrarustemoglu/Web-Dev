a = input().split()

for i in range(len(a) - 1):
    if int(a[i]) < int(a[i + 1]):
        print(a[i + 1], end=" ")