def replace(file,old_word,new_word):
    f=open(file)
    count=0
    content=[]
    for each_line in f:
        if old_word in each_line:
            count=each_line.count(old_word)
            each_line=each_line.replace(old_word,new_word)
        content.append(each_line) #把所有的文件重新写入一遍

    judge=input('文件%s中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】:'\
                %(file,count,old_word,old_word,new_word)) #%s是用来替换字符串的啊
    

    if judge=='YES':
        f1=open(file,'w')
        f1.writelines(content) #这一步是关键，把所有新写入的语句直接写入f1中
        f1.close()
        print('替换完成')
    
    f.close()           

file=input('请输入文件名：')
old_word=input('请输入需要替换的单词或字符：')
new_word=input('请输入新的单词或字符：')
replace(file,old_word,new_word)
