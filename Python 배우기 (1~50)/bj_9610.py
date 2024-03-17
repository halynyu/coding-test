"""
사분면

문제
2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다. 다음 n개 줄에는 점의 좌표 (xi, yi)가 주어진다. (-106 ≤ xi, yi ≤ 106)

출력
각 사분면과 축에 점이 몇 개 있는지를 예제 출력과 같은 형식으로 출력한다.
"""

n = int(input())
axis = 0
q1 = 0
q2 = 0
q3 = 0
q4 = 0

for _ in range(n) :
  x, y = map(int, input().split())
  
  if x == 0 or y == 0 :
    axis += 1
  elif x > 0 and y > 0 :
    q1 += 1
  elif x < 0 and y > 0 :
    q2 += 1
  elif x < 0 and y < 0 :
    q3 += 1
  else :
    q4 += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)