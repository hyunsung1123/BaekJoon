def solution(left, right):
    answer = 0
    for number in range(left,right+1):
        count=0
        for i in range(1,int(number**(1/2))+1): #약수는 하나가 정해지면 다른하나가 정해진다. 루트를 취한것까지 돌면된다.
            if number % i ==0 and i**2 != number: # 25의 경우 1 5 25이다.5는 2개가 아닌 1개로 취급해야하므로 해당 조건 넣음
                count+=2
            elif number % i==0:
                count+=1
        if count%2 ==0:
            answer+=number
        else:
            answer -=number
    return answer