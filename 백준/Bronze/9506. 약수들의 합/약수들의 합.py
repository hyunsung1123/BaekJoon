while True:
    N=int(input())
    A=[]
    sum=0
    b = ""
    if N==-1:
        break
    for i in range(1,N):
        if N%i ==0:
            A.append(i)
    for i in range(len(A)):
        sum += A[i]
        if i == len(A)-1:
             b= b+ str(A[i])
        else:
            b = b + str(A[i]) + " + "
    if N == sum:
            print(N,"=",b)
    else:
        print(N,"is NOT perfect.")