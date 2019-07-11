#shuzi = int(input('请输入色子点数：'))
#if shuzi == 1:
#    print("请唱歌！")
#elif shuzi == 2:
#    print("请跳舞！")
#elif shuzi == 3:
#    print("请吃饭！")
#elif shuzi == 4:
#    print("请喝酒！")
#elif shuzi == 5:
#    print("请吃鸡！")
#elif shuzi == 6:
#    print("请吃屎！")

from random import randint
face = randint(1,6)
if face == 1:
    print('唱首歌')
elif face == 2:
    print('跳个舞')
elif face == 3:
    print('学狗叫')
elif face == 4:
    print( '做俯卧撑')
elif face == 5:
    print('念绕口令')
else:
    print('讲冷笑话')
