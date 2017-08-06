import random as r

coordinate_x=[0,10]
coordinate_y=[0,10]


class turtle:
    def __init__(self):
        self.energy=100 #乌龟初始体力值
        
        self.x=r.randint(coordinate_x[0],coordinate_x[1]) #初始位置随机
        self.y=r.randint(coordinate_y[0],coordinate_y[1])

    def move(self):
        new_x=self.x+r.choice([0,-1,1,-2,2])#这个和本题目的要求并不是很对应
        new_y=self.y+r.choice([0,-1,1,-2,2])
        # 判断移动后的是否超出场景边界
        if new_x< coordinate_x[0]:
            self.x=coordinate_x[0]-(new_x-coordinate_x[0])
        elif new_x>coordinate_x[1]:
            self.x=coordinate_x[1]-(new_x-coordinate_x[0])
        else:
            self.x=new_x

        if new_y< coordinate_y[0]:
            self.y=coordinate_y[0]-(new_y-coordinate_y[0])
        elif new_y>coordinate_y[1]:
            self.y=coordinate_y[1]-(new_y-coordinate_y[0])
        else:
            self.y=new_y

        #体力消耗,这个地方当时怎么都没注意到
        self.energy -= 1
        return (self.x,self.y)
    
    def eat(self):
        if self.energy+20>=100:
            self.energy=100
        else:
            self.energy=self.energy+20

class fish:
    def __init__(self):
        self.x=r.randint(coordinate_x[0],coordinate_x[1])
        self.y=r.randint(coordinate_y[0],coordinate_y[1])

    def move(self):
        new_x=self.x+r.choice([0,-1,1])
        new_y=self.y+r.choice([0,-1,1])
        if new_x< coordinate_x[0]:
            self.x=coordinate_x[0]-(new_x-coordinate_x[0])
        elif new_x>coordinate_x[1]:
            self.x=coordinate_x[1]-(new_x-coordinate_x[0])
        else:
            self.x=new_x

        if new_y< coordinate_y[0]:
            self.y=coordinate_y[0]-(new_y-coordinate_y[0])
        elif new_y>coordinate_y[1]:
            self.y=coordinate_y[1]-(new_y-coordinate_y[0])
        else:
            self.y=new_y
        return (self.x,self.y)

Turtle=turtle()
Fish=[]
for i in range(0,10):
        each_fish = fish()
        Fish.append(each_fish)

while True:
        if Turtle.energy==0:
            print('乌龟体力已经耗尽')
            break

        if Fish==[]:
            print('小鱼已经吃光')
            break
    
        pos=Turtle.move()
    
        for each_fish in Fish:
            if pos==each_fish.move():
                Fish.remove(each_fish)
                Turtle.eat()
                print('有一条鱼儿被吃掉了···')
        


        
