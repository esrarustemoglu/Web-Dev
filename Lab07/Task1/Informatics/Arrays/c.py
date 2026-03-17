a = input().split()
count = 0
for i in range(len(a)):
    if int((a[i])) > 0:
        count +=1
print(count)