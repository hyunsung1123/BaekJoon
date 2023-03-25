while True:
    x,y,z=map(int,input().split(" "))
    if x==y==z==0:
        break
    if x+y+z-max(x, y, z) > max(x, y, z):
        if x==y==z:
            print("Equilateral")
        elif x==y or y==z or x==z:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")