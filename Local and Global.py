def discounts(price,rate):
    final_price = price * rate
    old_price = 88 #这里试图修改全局变量
    print('修改后old_price的值是1：', old_price)
    return final_price      # 局部变量
 
old_price = float(input('请输入原价：'))      #全局变量
rate = float(input('请输入折扣率：'))
new_price = discounts(old_price, rate)      #全局变量
print('修改后old_price的值是2：', old_price)
print('打折后价格是：', new_price)
