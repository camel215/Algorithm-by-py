# DFS문제
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().strip()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

three_cnt, two_cnt = 0, 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    # 현재 색상 좌표를 방문한다.
    visited[x][y] = True
    current_color = matrix[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx < n) and (0 <= ny < n):

            if visited[nx][ny] == False:
                if matrix[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            three_cnt += 1

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)