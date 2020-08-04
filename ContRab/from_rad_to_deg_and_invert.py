import math


'''
 x0 - изначальный х пушки
 x1 - 
 y0 - 
 y1 - 
 a1 - 
 b1 - 
''' 


x0 = 20 
x1 = 20
y0 = 450
y1 = 450
a1 = x1 - x0
b1 = y1 - y0
alfa = math.atan2(b1,a1)
print(45*math.pi/180)
print("alfa rad=",alfa, "alfa deg=",alfa*180/math.pi)
