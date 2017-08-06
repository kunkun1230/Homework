#单次判断，某一年是否为闰年
##year=input('请输入年份：')
##num=int(year)
##if num%100==0:
##    if num%400==0:
##        print(year,'年是闰年')
##    else:
##        print(year,'年是平年')
##else:
##    if num%4==0:
##        print(year,'年是闰年')
##       
##    else:
##        print(year,'年是平年')

#循环判断某一年是否为闰年
##year=input('请输入年份：')
##num=int(year)
##while 'c':  #这里加一个while语句，可以实现无限次输入数字，哈哈
##    if num%100==0:
##        if num%400==0:
##            print(year,'年是闰年')
##        else:
##            print(year,'年是平年')
##    else:
##        if num%4==0:
##            print(year,'年是闰年')
##        else:
##            print(year,'年是平年')
##    year=input('请输入年份：')
##    num=int(year)

#当输入的值不是整型时，将给予提示
##year=input('请输入年份：')
##num=0
##while 'c':  #这里加一个while语句，可以实现无限次输入数字，哈哈
##    while not year.isdigit(): #进一步加一个year.isdigit可以判断输入的格式是否是整型
##        year=input('格式错误，请重新输入：')
##    num=int(year)
##    if num%100==0:
##        if num%400==0:
##            print(year,'年是闰年')
##        else:
##            print(year,'年是平年')
##    else:
##        if num%4==0:
##            print(year,'年是闰年')
##        else:
##            print(year,'年是平年')
##    year=input('请输入年份：')


#只能猜3次，是否是闰年
##year=input('请输入年份：')
##num=0
##i=3
##while i>0:  #这里加一个while语句，可以实现无限次输入数字，哈哈
##    while not year.isdigit(): #进一步加一个year.isdigit可以判断输入的格式是否是整型
##        year=input('格式错误，请重新输入：')
##    i=i-1
##    num=int(year)
##    if num%100==0:
##        if num%400==0:
##            print(year,'年是闰年')
##        else:
##            print(year,'年是平年')
##    else:
##        if num%4==0:
##            print(year,'年是闰年')
##        else:
##            print(year,'年是平年')
##        if i>0:
##            print('还可以猜',i,'次')
##        else:
##            print('已经三次了，你没有机会了')
##            break
##    year=input('请输入年份：')


i = 5
while i > 0:#添加循环
    a = input('请输入一个闰年年份：')
    while not a.isdigit():#判断temp.isdigit()是否为真
        a = input('这是年份吗？再输入一次！')
    year = int(a)#给变量year赋值：整型
    if year/400 == int(year/400):#闰年计算方法，能够被400或者4整除
        print('恭喜你答对了'+ a + '是闰年！')
        print('good job')
        break#当条件成熟时终止循环
    else:
        print(a +'不是闰年！')
        i = i - 1
        if i > 0:
            print('try again')
        else:
            print('no chance,bye')
    
