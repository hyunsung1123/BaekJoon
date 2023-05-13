import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    C = int(input())
    Quarter = C//25  
    Dime = (C%25)//10
    Nickel = ((C%25)%10) // 5
    Penny = ((C%25)%10)%5
    print(Quarter,Dime,Nickel,Penny)