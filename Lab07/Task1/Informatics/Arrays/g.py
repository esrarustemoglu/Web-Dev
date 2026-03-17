a = input().split()

maximum = int(a[0])
index = 0

for i in range(len(a)):
    if int(a[i]) > maximum:
        maximum = int(a[i])
        index = i

print(maximum, index)