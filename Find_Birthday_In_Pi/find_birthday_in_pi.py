import matplotlib.pyplot as plt

file_name = "pi_a_hundred_million_digits.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:                                         # 将pi结合为一个字符串
    pi_string += line.strip()
print(len(pi_string))                                      # 统计pi的位数


def yymmdd(yy, mm, dd):
    # 获取格式为年月日的日期，输出为字符串类型
    if mm < 10 and dd < 10:
        return str(yy) + "0" + str(mm) + "0" + str(dd)
    elif mm < 10 <= dd:
        return str(yy) + "0" + str(mm) + str(dd)
    elif mm >= 10 > dd:
        return str(yy) + str(mm) + "0" + str(dd)
    else:
        return str(yy) + str(mm) + str(dd)


def leap_year(year_to_judge):
    # 判断是否是闰年
    if (year_to_judge % 4 == 0 and year_to_judge % 100 != 0) or year_to_judge % 400 == 0:
        return True
    else:
        return False


years = list(range(1960, 2000))                           # 想统计的年份跨度
dates = []
dates_in_list = []
number_list = []

for year in years:
    for month in [1, 3, 5, 7, 8, 10, 12]:
        for day in range(1, 32):
            dates.append(yymmdd(year, month, day))

    for month in [4, 6, 9, 11]:
        for day in range(1, 31):
            dates.append(yymmdd(year, month, day))

    for month in [2]:
        if leap_year(year):
            for day in range(1, 30):
                dates.append(yymmdd(year, month, day))
        else:
            for day in range(1, 29):
                dates.append(yymmdd(year, month, day))

    for date in dates:                                       # 在pi中寻找日期
        if date in pi_string:
            dates_in_list.append(date)

    print("Year " + str(year) + " has " + str(len(dates)) +
          " days in all, among which " + str(len(dates_in_list)) +
          " days can be found in the first one hundred million digits of pi.")

    with open("result_summary.txt", "a") as result_object1:
        result_object1.write("Year " + str(year) + " has " + str(len(dates)) +
                            " days in all, among which " + str(len(dates_in_list)) +
                            " days can be found in the first one hundred million digits of pi.\n")

    with open("result_data.txt", "a") as result_object2:
        result_object2.write(str(dates) + "\n" + str(len(dates)) + "\n" +
                             str(dates_in_list) + "\n" + str(len(dates_in_list)) + "\n")

    number = (round(len(dates_in_list)/len(dates), 4)) * 100
    number_list.append(number)
    dates.clear()
    dates_in_list.clear()

# 将数据以条形图的形式输出
"""
# 定义竖向条形图（适合于数据较少）
plt.figure(figsize=(10, 5))                                          # 定义画布大小
columns = plt.bar(range(len(number_list)), number_list, color="skyblue", align="center")
index = list(range(len(number_list)))
plt.ylim(top=100, bottom=0)                                          # 规定Y轴刻度范围
name_list = years.copy()
plt.xticks(index, name_list)                                         # 添加X轴刻度标签
plt.title("The proportion of birthdays in a year that can be found"  # 添加标题
          " in the first one hundred million digits of pi")
plt.xlabel("Years")                                                  # 添加X轴标签
plt.ylabel("Proportion(%)")                                          # 添加Y轴标签

for column in columns:                                               # 为柱体添加数值标签
    plt.text(
        # get_x()得到柱体左侧边缘坐标 get_height()得到柱体高度 get_width()得到柱体宽度
        column.get_x() + column.get_width() / 2,                     # 数值标签在X轴方向的坐标 在柱体居中位置
        column.get_height(),                                         # 数值标签在Y轴方向的坐标
        str(round(column.get_height(), 2)) + "%",                    # 数值标签内容
        ha="center",                                                 # horizontal align 横向居中对齐
        va="bottom"                                                  # vertical align 纵向底部对齐
    )
"""
# 定义横向条形图（适合于数据较多）
plt.figure(figsize=(10, 20))                                         # 定义画布大小
columns = plt.barh(range(len(number_list)), number_list, color="skyblue", align="center")
index = list(range(len(number_list)))
plt.xlim((0, 100))                                                   # 规定X轴刻度范围
name_list = years.copy()
plt.yticks(index, name_list)                                         # 添加Y轴刻度标签
plt.title("The proportion of birthdays in a year that can be found"  # 添加标题
          " in the first one hundred million digits of pi")
plt.ylabel("Years")                                                  # 添加Y轴标签
plt.xlabel("Proportion(%)")                                          # 添加X轴标签

for column in columns:                                               # 为柱体添加数值标签
    plt.text(
        # get_y()得到柱体下侧边缘坐标 get_height()得到柱体宽度 get_width()得到柱体高度
        column.get_width(),                                          # 数值标签在X轴方向的坐标
        column.get_y() + column.get_height() / 2,                    # 数值标签在Y轴方向的坐标 在柱体居中位置
        str(round(column.get_width(), 2)) + "%",                     # 数值标签内容
        ha="left",                                                   # horizontal align 横向左对齐
        va="center"                                                  # vertical align 纵向居中对齐
    )

plt.savefig("result.png")                                            # 保存图片
plt.show()                                                           # 显示图片
