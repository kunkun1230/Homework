##word=[]
##name=input('请输入文件名：')
##f=open(r'E:\\name.txt','w')
##
##content=input("请输入内容【单独输入':w'保存退出】：")
##word.append(content)
##f.writelines(word)
##
##for each_line in word:
##    if each_line == ':w':
##        f.close()

def file_write(file_name):
    f=open(file_name,'w')
    print('请输入内容【单独输入\':w\'保存退出】：')

    while True: #这个循环是程序的核心
        write_some=input()
        if write_some != ':w':
            f.write('%s\n'%write_some)
        else:
            break

    f.close()

file_name=input('请输入文件名')
file_write(file_name)
