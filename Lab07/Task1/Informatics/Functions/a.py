def min(a, b, c, d):
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    if d < minimum:
        minimum = d
    return minimum

a, b, c, d = map(int, input().split())
print(min(a, b, c, d))