class ticket():
    def __init__(self,adult=True,weekend=False):#默认是成人，如不是需声明，默认是工作日
        self.ticket=100
        if adult==True:
            self.discount=1
        else:
            self.discount=0.5

        if weekend==True:
            self.inc=1.2
        else:
            self.inc=1

    def price(self,num): #self指的是定义的函数本身，是具体的实例化对象的名字
        return self.ticket*self.discount*self.inc*num

adult=ticket()
child=ticket(adult=False)
num_adult=input('请输入成人数量：')
num_child=input('请输入小孩数量：')
total_price=adult.price(int(num_adult))+child.price(int(num_child))
print("%s个成人和%s个小孩的平日票价为%s"%(num_adult,num_child,total_price))
            
        
        
        
