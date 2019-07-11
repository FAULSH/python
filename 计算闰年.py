year = int(input("请输入年份："))
ls_leap = (year % 4 == 0 and year % 100 !=0
           or year % 400 == 0)
print(ls_leap)