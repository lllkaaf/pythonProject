
n = int(input())
x = 1
a = 1
sum = 0
while x < n:
    a = x * x
    sum = sum + a
    a = 0
    x += 1
    print(sum)


