a = input()
b=input()

count = 0

for digit in a:
    if digit == b:
        count += 1

print(count)