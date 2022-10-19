n = int(input())
if (n == 1 or n == 2):
    print(1)
else:
    first = 1
    second = 1
    for i in range(2, n):
        num = first+second
        first = second
        second = num
    print(second)
