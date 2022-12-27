#import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
given = list(map(int, input().split()))



def binary_search(item, llst):
    start = 0
    end = n - 1
    
    while start <= end:
        mid = (start + end) // 2
        if item == llst[mid]:
            return 1
        elif item > llst[mid]:
            start = mid + 1
        elif item < llst[mid]:
            end = mid - 1
    return 0


for i in range(m):
    print(binary_search(given[i], lst))