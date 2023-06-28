# 거의 소수
import sys
input = sys.stdin.readline
a,b = map(int,input().split())

prime_num = [i for i in range(int(b**0.5)+1)]

# n까지 소수 리스트를 반환
def is_eratos(b):
    for i in range(2,int(b**0.5)+1):
        if prime_num[i] == 0: continue
        for j in range(i*i,int(b**0.5)+1,i):
            prime_num[j] = 0
    return prime_num

prime_num = is_eratos(b)
cnt = 0

for i in range(2,int(b**0.5)+1):
    if prime_num[i] != 0:
        num = prime_num[i]
        tmp = num*num
        while tmp <= b:
            if tmp >= a:                     
                cnt += 1

            tmp *= num

print(cnt)