a = input().split()
count = 0
for i in range(1, len(a) - 1):
    if int(a[i]) > int(a[i-1]) and int(a[i + 1]) < int (a[i]):
        count += 1
print(count)