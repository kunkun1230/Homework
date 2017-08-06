for i in range(0,4):
    for j in range(0,4):
        for k in range(2,7):
            if i+j+k==8:
                print('红球',i,'个','黄球',j,'个','蓝球',k,'个')
                
##print('red\tyellow\tblue')
##for red in range(0, 4):
##    for yellow in range(0, 4):
##        for green in range(2, 7):
##            if red + yellow + green == 8:
##                # 注意，下边不是字符串拼接，因此不用“+”哦~
##                print(red, '\t', yellow, '\t', green)
