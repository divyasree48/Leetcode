
t=int(input())
while(t):
    a,y,z=map(int,input().split())
    x=a*y*2
    if x>z:
        print(0)
    else:
        print(z//x)
    t-=1