wage = float(input("请输入个人工资:"))
mamy = float(input("请输入你的五险一金："))
chaji = wage - mamy - 3500
if chaji <=0 :
    rate = 0
    deduction = 0
elif chaji < 1500:
    rate = 0.03
    deduction = 0
elif chaji <= 4500:
    rate = 0.1
    deduction = 105
elif chaji <=9000 :
    rate = 0.2
    deduction = 555
elif chaji <=35000:
    rate = 0.25
    deduction = 1005
elif chaji <= 55000:
    rate = 0.3
    deduction = 2755
elif chaji <=80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(chaji * rate - deduction)
print('个人所得税： ￥%.2f元' % tax)
print('实际到手收入： ￥%.2f元' % (chaji + 3500 -tax))