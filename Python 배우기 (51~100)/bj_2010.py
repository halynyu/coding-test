# 플러그

import sys
input = sys.stdin.readline


n = int(input())
total = 0

for _ in range(n):
    total += int(input())

print(total-(n-1))


"""
import sys
input = sys.stdin.readline

이 부분 빼고했을 때는 시간초과뜸!!
"""