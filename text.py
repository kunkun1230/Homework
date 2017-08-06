##def fun(var):
##    var = 1314
##    print(var)
##var = 520
##fun(var)
##print(var)

##var = ' Hi '
##def fun1():
##    global var
##    var = ' Baby '
##    #return var
##    return fun2(var)
##def fun2(var):
##    var += 'I love you'
##    fun3(var)
##    return var
##def fun3(var):
##    var = ' 小甲鱼 '
##print(fun1())

def sentence():
    sentence=input('请输入一句话：')
    if sentence==sentence[::-1]:
        print('是回文联！')
    else:
        print('不是回文联！')
