# 피보나치 수 2

n = int(input())

f1=1
f2=1

for i in range(1, n+1):
    if i<=2:
        fn=1
    else:
        fn=f1+f2
        f1=f2
        f2=fn

print(fn)