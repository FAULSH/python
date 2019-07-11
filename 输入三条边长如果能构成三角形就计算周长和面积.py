x = float(input('x= '))
y = float(input('y= '))
z = float(input('z= '))
perimeter = x + y + z
p = (perimeter/2)
import math
area = math.sqrt(p*(p-x)*(p-y)*(p-z))
if x + y >z and x + z > y and y +z >x:
    print("周长：", perimeter)
    print("面积：", area)
else:
    print("不能构成三角形")
#import math
#a = float(input('a = '))
#b = float(input('b = '))
#c = float(input('c = '))
#if a + b > c and a + c > b and b + c > a:
#    print('周长: %f' % (a + b + c))
#    p = (a + b + c) / 2
#    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
#    print('面积: %f' % (area))
#else:
#    print('不能构成三角形')