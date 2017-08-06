def findstr():
    sentence=input('请输入目标字符串：')
    word=input('请输入子字符串（两个字符）：')
    a=sentence.count(word)
    print('子字符串在目标字符串中共出现',a,'次')
