# 별 찍기 - 6

n = int(input())

for i in range(n):
    print(" "*(2*n-i), end="")
    print("*"*(n-i))