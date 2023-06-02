import sys
input = sys.stdin.readline

def merge_sort(A,low,high):
    if (low<high and cnt <= K):
        mid = (low+high)//2
        merge_sort(A,low,mid)
        merge_sort(A,mid+1,high)
        merge(A,low,mid,high)
def merge(A,low,mid,high):
    global cnt, ans
    i= low; j=mid+1; t=0
    tmp = []
    while(i<=mid and j<=high):
        if A[i]<A[j]:
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1
        t+=1
    while(i<=mid):
        tmp.append(A[i])
        i+=1
        t+=1
    while(j<=high):
        tmp.append(A[j])
        j+=1
        t+=1
    i=low; t=0
    while(i<=high):
        A[i] = tmp[t]
        cnt +=1
        if cnt == K:
            ans = A[i]
            break
        i+=1
        t+=1
N,K = map(int,input().strip().split())
A = list(map(int,input().strip().split()))
cnt = 0
ans = -1
merge_sort(A,0,len(A)-1)
print(ans)