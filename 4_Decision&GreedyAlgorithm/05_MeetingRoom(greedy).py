'''
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 
회의실 사용표를 만들려고 한다. 각 회의에 대해 시작시간과 끝나는 시간이 
주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 
최대수의 회의를 찾아라. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.

There is one meeting room, and you need to make a schedule table 
of room usage for the n number of meetings that needs to use the meeting room. 
Find the maximum number of meetings that can use the meeting room. 
You will be given the start time and an end time for each meeting, 
and the usage cannot be overlapping each other. 
Once a meeting is started, it cannot be interrupted in the middle, 
and the next meeting may begin at the same time as one meeting ends.
'''


import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]


'''
회의가 끝나는 시간을 기준으로 정렬.
왜 시작시간으로 안하냐? -> 우리는 회의를 최대한 많이 해야하는데, 시작시간이 빠르다 해서 빨리 끝나는게 아니니까... 
시작시간 빠른 애 골랐다가 막 7시간짜리 고를 수도 ㅇ.
빨리 끝나는게 중요함!
첫번쨰 회의를 제일 빨리 끝나는 애로 하고, 그 회의의 끝나는 시간과 그 다음으로 빨리 끝나는 회의의 시작 시간이 크거나 같은 애 선택. 
'''

# 이차원 배열의 두번째 키를 기준으로 정렬하기 위해 key와 람다함수 사용

lst.sort(key=lambda x: x[1])

cnt = 1
endtime = lst[0][1]  
for i in range(n):
    if lst[i][0] >= endtime:
        cnt += 1
        endtime = lst[i][1]
        
print(cnt)
