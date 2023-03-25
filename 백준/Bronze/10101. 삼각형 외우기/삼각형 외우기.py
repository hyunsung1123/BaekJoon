A=int(input())
B=int(input())
C=int(input())

Sum = A+B+C
if Sum!=180:
    print("Error")
elif A==B==C:
    print("Equilateral")
elif A==B or B==C or A==C: 
    print("Isosceles")
else:
    print("Scalene")
