# 내 학점을 구해줘

t = int(input())

for _ in range(t):
    n = int(input())
    total_c = 0
    total = 0
    for _ in range(n):
        c, g = input().split()
        total_c += int(c)
        total += int(c)*float(g)
    print(f"{total_c} {total/total_c:.01f}")
        