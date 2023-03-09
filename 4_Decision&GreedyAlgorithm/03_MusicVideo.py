'''
지니레코드에서는 불세출의 가수 조영필의 라이브 동영상을 DVD로 만들어 판매하려 한다.
DVD에는 총 N개의 곡이 들어가는데, 
DVD에 녹화할 때에는 라이브에서의 순서가 그대로 유지되어야 한다. 
순서가 바뀌는 것을 우리의 가수 조영필씨가 매우 싫어한다. 
즉, 1번 노래와 5번 노래를 같은 DVD에 녹화하기 위해서는 
1번과 5번 사이의 모든 노래도 같은 DVD에 녹화해야 한다. 
또한 한 노래를 쪼개서 두 개의 DVD에 녹화하면 안된다.
지니레코드 입장에서는 이 DVD가 팔릴 것인지 확신할 수 없기 때문에 
이 사업에 낭비되는 DVD를 가급적 줄이려고 한다. 
고민 끝에 지니레코드는 M개의 DVD에 모든 동영상을 녹화하기로 하였다. 
이 때 DVD의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 
그리고 M개의 DVD는 모두 같은 크기여야 제조원가가 적게 들기 때문에 
꼭 같은 크기로 해야 한다.

Genie Records is planning to make a DVD 
of the singer Cherrie's live singing video.
A total of N songs are included in the DVD, 
and the order of songs sung in live must be maintained when saved on the DVD. 
Our singer Cherrie hates changing the order of songs. 
In other words, in order to record song #1 and song #5 on the same DVD, 
all songs between song #1 and #5 must also be recorded on the same DVD. 
Also, you should not split a song and record it on two DVDs.
Genie Records is not sure if the DVD will be sold, 
so they try to reduce the amount of DVDs wasted on the business as much as possible. 
After much consideration, Genie Records decided to record 
all the videos on M number of DVDs. 
The size(recordable length) of the DVD is to be minimized. 
And all M DVDs must be the same size, because that would cost less to manufacture.
'''


import sys
#sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# dvd 개수 새줌.
def countDvd(arr, num):
    cnt = 1
    sum = 0
    for i in range(len(arr)):
        # i 번째 노래를 더했을 때 허용량보다 큼
        if sum + arr[i] > num:
            cnt += 1  # dvd 하나 추가
            sum = arr[i]
        else: 
            sum += arr[i]
    return cnt

res = 0
lo, hi = 1, sum(lst)

while lo <= hi:
    mid = (lo + hi) // 2
    
    if countDvd(lst, mid) <= M: # 용량 충분함
        res = mid
        hi = mid - 1
    else: # 용량 너무 작음
        lo = mid + 1
        
print(res)
    
