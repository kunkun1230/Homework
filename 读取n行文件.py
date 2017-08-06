##def print_n_line(file,n):
##    f=open(file)
##    for i in range(n):
##        print(f.readline(),end='') #一次读取一行
##
##    f.close
## 
##    
##file=input('请输入要打开的文件(c:\\test.txt):')
##n=int(input('请输入需要显示该文件的前几行：'))
##print_n_line(file,n)

def print_n_line(file,n):
    f=open(file)
    a=list(f)
    (num1,num2)=n.split(':',1)
    if num1 =='':
        num1=0
    if num2 =='':
        num2=len(a)
    f.seek(0)
    for i in range(int(num1),int(num2)):
        print(a[i],end='')

    f.close
   
file=input('请输入要打开的文件(c:\\test.txt):')
n=input('请输入需要显示该文件行数【格式如13:21】：')
print_n_line(file,n)


