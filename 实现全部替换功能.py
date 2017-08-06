
def replace(old_word,new_word):
    f=open(file_name)
    a=f.read()
    b=a.count(old_word)
    print('文件%s中共有%s个【%s】'%(file_name,b,old_word))#原来格式化中%s是可以直接替换数字的
    print('您确定把所有的【%s】替换为【%s】吗？'%(old_word,new_word))
    judge=input('【YES/NO】:')
    if judge=='YES'or judge=='Yes'or judge =='yes':# if judge in ['Yes','YES','yes']
        c=a.replace(old_word,new_word)
        print('替换成功')
    else:
         f.close()

    f.close
    f=open(file_name,'w')
    f.write(c)
    f.close

file_name=input('请输入文件名：')
old_word=input('请输入需要替换的单词或字符：')
new_word=input('请输入新的单词或字符：')
replace(old_word,new_word)

    
