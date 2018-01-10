# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:28:02 2018

@author: lenovo
"""

x=0.06
y=1
while y > 0.1 or y < -0.1:
    xx= input('请输入x的值')
    x=float(xx)
#    print('10万以年复利计息')
#    y=100000*(1+12*x)**5-2000*(1+x)*((1+x)**60-1)/x
    print('10万以月复利计息')
    y=100000*(1+x)**60-2000*(1+x)*((1+x)**60-1)/x
    print(y)
    
    