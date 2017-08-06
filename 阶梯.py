i=1
while i:
    if ((i%2==1)and (i%3==2) and (i%5==4)and(i%6==5)and(i%7==0))==True:
        print('该阶梯至少有',i,'阶')
        break
    else:
        print(end="")
    i+=1
