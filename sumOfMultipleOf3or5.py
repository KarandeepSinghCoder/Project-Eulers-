import math
t = int(input())
a = []
if (t >= 1 and t <= 100000):
    for i in range(t):
        n = int(input())
        a.append(n)

for i in range(t):
    if(a[i]>=1 and a[i]<=1000000000):

        n1=math.floor((a[i]-1)/3);
        n2=math.floor((a[i]-1)/5);
        n3=math.floor((a[i]-1)/15);
        sum =((3*n1*(n1+1))+(5*n2*(n2+1))-(15*n3*(n3+1)))//2
        print(int(sum))