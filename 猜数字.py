temp=input('请输入数字')
guess=int(temp)
while guess!=8:
    temp=input('哎呀，猜错啦，请重新输入吧:')
    guess=int(temp)
    if guess==8:
            print('哥，你真牛逼')
    else:
            if guess>8:
                    print('哥，大了大了')
            else:
                    print('哥，小了小了')
print('游戏结束，不玩啦')
