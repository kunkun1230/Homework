##Passcode=input('请输入要检查的密码组合：')
##length=len(Passcode)
##word=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
##num=(0,1,2,3,4,5,6,7,8,9)
##i,j,k=0,0,0
##while length<=8:
##    if Passcode.isalnum()==True:
##        print('这是低级密码')
##        break
##    else:
##        print('8位以下，但密码输入错误')
##        break
##while (length>=16) and (Passcode[0]in word==True) and (Passcode.isallnum()==False):
##    while i<length:
##        if Passcode[i] in word==True:
##            j=j+1
##        elif Passcode[i] in num==True:
##            k=k+1
##    i+=1
##    if (j>1==True) and (k>1==True):
##        print('这是高级密码')
##        break
##    else:
##        print('16位以上，但密码格式输入错误')
##        break

symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' #字母库里面大小写都有的，且写成了一个字符串
nums = '0123456789'
 
passwd = input('请输入需要检查的密码组合：')
 
# 判断长度
length = len(passwd)
 
while (passwd.isspace() or length == 0) :
    passwd = input("您输入的密码为空（或空格），请重新输入：")
 
if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len = 3
 
flag_con = 0
 
# 判断是否包含特殊字符
for each in passwd:
    if each in symbols:
        flag_con += 1
        break
    
# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break
 
# 判断是否包含数字
for each in passwd:
    if each in nums:
        flag_con += 1
        break    
 
# 打印结果
while 1 :
    print("您的密码安全级别评定为：", end='')
    if flag_len == 1 or flag_con == 1 :
        print("低")
    elif flag_len == 2 or flag_con == 2 :
        print("中")
    else :
        print("高")
        print("请继续保持")
        break
 
    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位'")
    break
