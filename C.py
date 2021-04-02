
def cal():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return 0
    ans = 1 << 30
    for i in range(1, 1 << (n - 1)):
        now = 0
        OR = 0
        for j in range(0, n):
            OR |= a[j]
            if i >> j & 1:
                now ^= OR
                OR = 0

        now ^= OR
        ans = min(ans, now)

    print(ans)
    return 0

cal()


