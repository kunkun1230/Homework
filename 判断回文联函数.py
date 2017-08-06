def sentence():
    sentence=input('请输入一句话：')
    if sentence==sentence[::-1]:
        print('是回文联！')
    else:
        print('不是回文联！')
