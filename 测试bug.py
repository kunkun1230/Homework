import sys
try:
    s = input('Enter something --> ')  #可能得到异常的语句
except EOFError:       #锁定是哪种异常
    print ('ERROR INPUT !')   #出现异常的处理方法
    sys.exit()
print (s)
