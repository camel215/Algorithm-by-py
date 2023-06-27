# 숫자 야구
import sys
input = sys.stdin.readline
import itertools
case = list(itertools.permutations([i for i in range(1,10)],3))
ans = 0

games = [list(map(int,input().split())) for _ in range(int(input()))]

for i in case:
    check = True
    for game in games:
        s,b = 0,0
        for j in range(3):
            if str(i[j]) == str(game[0])[j]:
                s += 1
            elif str(i[j]) in str(game[0]):
                b += 1
        if s != game[1] or b != game[2]:
            check = False
            break
    if check:
        ans +=1

print(ans)