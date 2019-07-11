#results = float(input("请输入你的成绩："))
#if results >= 90:
#    print("你的成绩等级为：A")
#elif 80 <=results <= 89:
#    print("你的成绩等级为：B")
#elif 70 <= results <= 79:
#    print("你的成绩等级为：C")
#elif 60 <=results <= 69:
#    print("你的成绩等级为：D")
#else:
#    print("你的成绩等级为：E")

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)