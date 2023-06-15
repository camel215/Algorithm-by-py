import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
area = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def BFS(x,y,h):
    ### 초기 큐 설정 ###
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx,cy = queue.popleft()
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if (nx >= 0 and nx<n) and (ny >= 0 and ny<n):
                if not visited[nx][ny] and area[nx][ny] > h:
                    queue.append((nx,ny))
                    visited[nx][ny] = True

m = 1
for h in range(101):
    visited = [[False]*n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > h:
                BFS(i,j,h)
                count += 1
    
    m = max(m,count)

    if count == 0:
        break

print(m)