def evenfibsum(n):
    if(n<=2):
        return 0
    else:
        a=0
        b=2
        s=a+b
        while(b<=n):
            c=4*b+a
            if(c>=n):
                break
            a=b
            b=c
            s+=b
        return s
a=[]
t=int(input())
if(t>=1 and t<=100000):
    for i in range(t):
        n=int(input())
        a.append(n)

    for i in range(t):
        if(a[i]>=1 and a[i]<=40000000000000000):
            print(evenfibsum(a[i]))
