def arithmetic(n):
   # for i in range(1,n):   注意递归里面不需要这句话
    if n==1:
        return 1
    else:
        return n+arithmetic(n-1)

