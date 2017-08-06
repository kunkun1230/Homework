##i=2
##password='kunkun'
##code=input('请输入密码：')
##while i:
##    if code==password:
##        print('密码输入正确')
##        break
##    else:
##        code=input('密码输入错误，请重新输入')
##    i=i-1
##    if i==0:
##        print('三次机会已经用尽')

i=3
password='kunkun'
#code=input('请输入密码：') 有这个命令第一次输入正确与否都不会提示
while i:
    code=input('请输入密码：') #注意这里一定再加一次input命令
    if code==password:
        print('密码输入正确')
        break
    elif "*" in code:
        print('密码中不能有*，请重新输入：')
        continue #注意
    else:
        code=print('密码输入错误')
    i=i-1#注意这里的缩进情况
    if i==0:
        print('三次机会已经用尽')


