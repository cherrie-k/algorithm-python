import sys
from copy import deepcopy
#sys.stdin = open("input.txt", "rt")

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))



def move_up(lst):
    for j in range(N):
        ptr = 0
        for i in range(1, N):
            if lst[i][j]:
                tmp = lst[i][j]
                lst[i][j] = 0
                # 포인터가 가리키는게 0일 때
                if lst[ptr][j] == 0:
                    lst[ptr][j] = tmp
                # 포인터가 가리키는거랑 현재 위치의 수가 같을 때
                elif lst[ptr][j] == tmp:
                    lst[ptr][j] *= 2
                    ptr += 1
                # 포인터가 가리키는거랑 현재 위치 수가 다를 때
                else:
                    ptr += 1
                    lst[ptr][j] = tmp
    return lst


def move_down(lst):
    for j in range(N):
        ptr = N - 1
        for i in range(N - 2, -1, -1):
            if lst[i][j]:
                tmp = lst[i][j]
                lst[i][j] = 0
                # 포인터가 가리키는게 0일 때
                if lst[ptr][j] == 0:
                    lst[ptr][j] = tmp
                # 포인터가 가리키는거랑 현재 위치의 수가 같을 때
                elif lst[ptr][j] == tmp:
                    lst[ptr][j] *= 2
                    ptr -= 1
                # 포인터가 가리키는거랑 현재 위치 수가 다를 때
                else:
                    ptr -= 1
                    lst[ptr][j] = tmp
    return lst


def move_left(lst):
    for i in range(N):
        ptr = 0
        for j in range(1, N):
            if lst[i][j]:
                tmp = lst[i][j]
                lst[i][j] = 0
                # 포인터가 가리키는게 0일 때
                if lst[i][ptr] == 0:
                    lst[i][ptr] = tmp
                # 포인터가 가리키는거랑 현재 위치의 수가 같을 때
                elif lst[i][ptr] == tmp:
                    lst[i][ptr] *= 2
                    ptr += 1
                # 포인터가 가리키는거랑 현재 위치 수가 다를 때
                else:
                    ptr += 1
                    lst[i][ptr] = tmp
    return lst


def move_right(lst):
    for i in range(N):
        ptr = N - 1
        for j in range(N - 2, -1, -1):
            if lst[i][j] :
                tmp = lst[i][j]
                lst[i][j] = 0
                # 포인터가 가리키는게 0일 때
                if lst[i][ptr] == 0:
                    lst[i][ptr] = tmp
                # 포인터가 가리키는거랑 현재 위치의 수가 같을 때
                elif lst[i][ptr] == tmp:
                    lst[i][ptr] *= 2
                    ptr -= 1
                # 포인터가 가리키는거랑 현재 위치 수가 다를 때
                else:
                    ptr -= 1
                    lst[i][ptr] = tmp
    return lst


def dfSearch(lst, cnt):
    if cnt == 5:
        # 2차원 배열 요소 중 가장 큰 값 반환
        return max(map(max, lst))
    
    # 상하좌우로 움직여 리턴한 값들 중 가장 큰 값 반환
    #  반드시 lst를 deepcopy해서 함수를 거친 lst값이 다음 함수에 들어가지 못하도록 해줘야함
    return max(dfSearch(move_up(deepcopy(lst)), cnt + 1), dfSearch(move_down(deepcopy(lst)), cnt + 1), dfSearch(move_left(deepcopy(lst)), cnt + 1), dfSearch(move_right(deepcopy(lst)), cnt + 1))

print(dfSearch(lst, 0))