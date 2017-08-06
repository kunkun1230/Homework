def compare_file(file1,file2):
    f1=open(file1)
    f2=open(file2)
    list1=list(f1)
    list2=list(f2)
    length1=max(len(list1),len(list2))
    count=0
    line_num=[]
    for each in range (0,length1):
        #print('两文件共有【%d】处不同'%count)
        if list1[each]!= list2[each]:
            #print('第%d行不一样'%(each+1))
            count+=1
            line_num.append(each)

    print('两文件共有【%d】处不同'%count)
    for each1 in line_num:
        print('第%d行不一样'%(each1+1))
  

file1=input('请输入需要比较的头一个文件名：')
file2=input('请输入需要比较的另一个文件名：')
compare_file(file1,file2)
