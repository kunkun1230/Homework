#用while 输入1-10
##temp=input('请输入一个整数：')
##num=int(temp)
##i=1
##while num:
##    print(i)
##    num=num-1
##    i=i+1

temp=input('请输入一个整数：')
num=int(temp)
while num: #循环输入的数字次数，直到0
    i=num-1 #变量赋值
    while i:
        print(' ',end='')
        i=i-1
    j=num
    while j:
        print('*',end='')
        j=j-1
    k=num
    while k:
        print('$',end='')
        k=k-1
    print()
    num=num-1
    
