##猜指定数字
##num=input('请输入数字')
##abc=int(num)
##while abc!=9:
##    num=input('猜错了，请重新输入吧：')
##    abc=int(num)
##    if abc>9:
##            print('哥，大了大了')
##    else:
##        if abc<9:
##                print('哥，小了小了')
##        else:
##                print('你是小甲鱼心里的蛔虫嘛');print('猜对了也没有奖励')
##print('游戏结束')

##随机猜数字 
##import random
##num=random.randint(1,10) #输入随机函数
##num1=input('请输入数字吧：')
##guess=0
##while guess!=num :
##    num1=input('猜错啦，请重新输入吧：') #1
##    while not num1.isdigit(): #这个修改，可以提示如果输入的不是数字
##        num1=input('格式输入错误')
##    #num1=input('猜错啦，请重新输入吧：') #2
##    #注意#1 #2，这两个语句的位置。#2位置等于跳过了判断字母的过程，所以这里如果再出现字母，则会报错，而#1语句则不会出现问题
##    guess=int(num1)
##    if guess >num:
##        print('哥，太大了')
##    else:
##        if guess<num:
##            print('哥，小了小了')
##        else:
##            print('猜对了，哈哈')
##print('游戏结束')


##随机猜数字，且只给三次机会
import random
times=3
secret=random.randint(1,10)
print('猜数字')
print('猜猜我心里想的是什么数字？',end='')
guess=0
while (guess != secret) and (times>0):
    temp=input()
    while not temp.isdigit():
        temp=input('输入格式错误：')
    guess=int(temp)
    times=times-1 #每输入一次，可用机会减一
    if guess==secret:
        print('尼玛，真牛逼')
    else:
        if guess>secret:
            print('哥，大了大了')
        else:
            print('哥，小了小了')
        if times>0:   #之前失败的原因是，不知道时间也有一个判断语句
            print('再试一次吧：',end='')
        else:
            print('机会用完，退下吧')
print('game over')
