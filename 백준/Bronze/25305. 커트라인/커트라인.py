N, k = map(int,input().split(" "))
Score = list(map(int,(input().split(" "))))
Score.sort(reverse=True)
print(Score[k-1])