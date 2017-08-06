
def statistic(x):
    word=0
    number=0
    space=0
    other=0
    for n in range (len(x)):
        for i in x[n]:
            if i.isalpha():
                word+=1
            elif i.isdigit():
                number+=1
            elif i==' ':
                space+=1
            else:
                other+=1
        print('第',n+1,'个字符串共有：',\n\
        \t '英文字母',word,'个,数字',\n\
        \t number,'个，空格',space,'个，其他字符',other,'个')



##def count(*param):
##    length = len(param)
##    print(param)
##    print('length的长度是',length)
##    for i in range(length): #确定元组中每一个元素的序号，以便最后打印
##        letters = 0
##        space = 0
##        digit = 0
##        others = 0
##        for each in param[i]:
##            if each.isalpha():
##                letters += 1
##            elif each.isdigit():
##                digit += 1
##            elif each == ' ':
##                space += 1
##            else:
##                others += 1
##        print('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。' % (i+1, letters, digit, space, others)) #原来格式化是可以这么用的，碉堡了
        
        
    
