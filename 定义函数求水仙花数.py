def fun2():
    for x in range(100,1000):
        a=x-100*(x//100)
        if x==pow(x//100,3)+pow(a//10,3)+pow(x%10,3):
            print(x)
    
