##score=int(input('请输入你的分数'))
##if 60<score <=80:
##    print('C')
##elif 60>=score:
##    print('D')
##elif 80<= score<90:
##    print('B')
##elif 90<=score<=100:
##    print('A')

##x,y,z=6,8,9
##small=x if x<y else y
##small=z if z<small else small
##print(small)

x,y,z=6,8,9
small=x if (x<y and x<z) else (y if y<z else z)
print(small)

