import sys
input = sys.stdin.readline

def isPalindrome(s, l , r, count):
    count+=1
    if l<r:
        if s[l] != s[r]:
            return 0,count
        else:
            return isPalindrome(s,l+1,r-1,count)
    else:
        return 1, count
    
T = int(input())
for _ in range(T):
    my_input = input().strip()
    count=0
    print(*isPalindrome(my_input,0,len(my_input)-1,count))
