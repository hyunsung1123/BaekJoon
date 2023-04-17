def recursion(s,low,high,count):
    if low >= high:
        return (1,count)
    elif s[low] != s[high]:
        return (0,count)
    else:
        count+=1
        return recursion(s,low+1,high-1,count)
def isPalindrome(s):
    count=1
    return recursion(s,0,len(s)-1,count)
a = int(input())
for i in range(a):
    str_input = input()
    print(*isPalindrome(str_input))