"""
从控制台中输入半径的值，计算输出出圆的面积
"""
radius = eval(input("Enter radius:\n"))
area = radius ** 2 * 3.14
# 格式化输出,输出变量用%()包裹
print("radius id %d ; area is %.2f" % (radius, area))
