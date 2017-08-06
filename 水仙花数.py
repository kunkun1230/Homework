##for x in range(1,10):
##    for y in range(0,10):
##        for z in range(0,10):
##            A=100*x+10*y+z
##            if A==x**3+y**3+z**3:
##                print(A)

for i in range(100,1000):
    x=int(i/100)
    s=(i-100*x)/10
    y=int(s)
    z=i-100*x-10*y
    while i==x**3+y**3+z**3:
        print(i)
    continue
