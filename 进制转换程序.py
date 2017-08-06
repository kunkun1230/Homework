word=input('请输入一个整数(输入Q结束程序)：')
if word=='Q':
          print('程序结束')
while word!='Q': 
        num=int(word)
        print('十进制->十六进制：',num,'->','%x'%num)
        print('十进制->八进制：',num,'->','%o'%num)
        print('十进制->二进制：',num,'->',bin(num))
        word=input('请输入一个整数(输入Q结束程序)：')
