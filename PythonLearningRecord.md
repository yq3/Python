# Python Learning Record
基础知识小结（来源于Mike Dane's Giraffe Academy 以及 Eric Matthes's Python Crash Course）  
### 变量的命名和使用  
* 变量名只能包含字母、数字和下划线，可以字母或下划线打头，但不能以数字打头
* 慎用小写字母l和大写字母O，可能会被误认为数字1和0
### 字符串string
```
name.title()            # 首字母大写
name.upper()            # 全部大写
name.lower()            # 全部小写
name.isupper()          # 判别是否是大写
len(name)               # 字符串的长度
print(name[0])          # 按位显示
name.strip()            # 剔除字符串两端的空白
```
制表符\t  
换行符\n  
### 数字number
```
print(10 % 3)                  # 取余/求模
print(3 ** 3)                  # 乘方
my_num = 5
print(str(my_num) + " apples")
print(abs(my_num))             # 绝对值
print(pow(3, 2))               # 幂
print(max(3, 2))               # 取大值
print(round(3.7))              # 四舍五入
from math import *
print(floor(3.7))              # 舍去小数
print(ceil(3.2))               # 有小数便加一
print(sqrt(9))                 # 开方根
```
```
# Building a Basic Calculator
num1 = input("enter a number: ")           # num1存储的是string类型
num2 = input("enter another number: ")
result = float(num1) + float(num2)         # 将string类型转化为float类型
print(result)
```
### 列表list
```
friends = ["Jack", "Kim", "Amy", "Mike", "Bob"]
numbers = [2, 4, 6]   
friends[1] = "Carl"                 # 修改第二个元素
print(friends[0])                   # 第一个
print(friends[-1])                  # 倒数第一个
print(friends[-2])                  # 倒数第二个
print(friends[1:])                  # 从1往后
print(friends[1:3])                 # 从1到3不包括3              
friends.extend(numbers)             # 把两个list加到一起
friends.append("Dave")              # 添加一个元素到末尾（常用于创建一个空列表 然后往里添加新元素）
friends.insert(1, "Ellen")          # 添加一个元素到某一位置 原始元素将被右移
del friends[0]                      # 移除某元素
friends.remove("Bob")               # 移除某元素
friends.clear()                     # 清除列表
friends.pop()                       # 弹出（清除）最后一个元素 弹出的元素可被使用
friends.pop(0)                      # 弹出指定的一个元素
print(friends.index("Mike"))        # 检测MIke是否在list里面
print(friends.count("Mike"))        # mike在list里面出现了几次
friends.sort()                      # 按字母顺序排序
friends.sort(reverse=True)          # 按字母顺序的相反顺序排序
friends.sorted()                    # 暂时按字母顺序排序
numbers.sort()                      # 按升序排序
numbers.reverse()                   # 颠倒顺序（与原顺序相比）
friends2 = friends.copy()           # 复制list

max(numbers)                        # 针对数字列表的一些操作
min(numbers)
sum(numbers)

for friend in friends:              # 利用for循环针对列表中的每一个元素进行操作
    print(friend)
    
number_grid = [                     # 2D lists 即列表的嵌套使用
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][2])            # 第二行第三列
for row in number_grid:             # for的嵌套使用
    for col in row:
        print(col)
```
```
numbers = list(range(1, 6))                      # 利用list()和range()创建数字列表
print(numbers)                                   # [1, 2, 3, 4, 5]

even_numbers = list(range(2, 11, 2))             # range()函数可以指定步长
print(even_numbers)                              # [2, 4, 6, 8, 10]

squares = [value**2 for value in range(1, 6)]    # 利用列表解析创建数字列表：列表名=[表达式 for循环给表达式提供值]
print(squares)                                   # [1, 4, 9, 16, 25]
```
### 元组tuple
不能修改元素，但可以给元组重新赋值  
```
coordinates = (4, 5)  
```
### if语句
相等==  
不等!=  
```
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:        
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
```
if-elif-else结构比较适合于只有一个条件满足的情况，如果要检查的条件很多，可以使用多个简单if语句  
```
numbers = []
if numbers:                     # if后面跟列表名 用以检查列表是否为空
    do something
else:
    do something
```
### 字典dictionary
```
month_conversions = {           # dictionary key-value pair
    "Jan": "January",           # key需要唯一
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(month_conversions["Jan"])                         # 通过key访问value
print(month_conversions.get("Jn"))                      # 使用get函数如果没有这个key会显示none 而不会报错
print(month_conversions.get("Jn", "Not a valid key"))   # 赋予它一个默认值
month_conversions["abc"] = "def"                        # 添加key-value pair
month_conversions["abc"] = "DEF"                        # 修改key对应的value
del month_conversions["abc"]                            # 删除key-value pair
for key, value in month_conversions.items():            # 遍历所有pair
    print(key, value)
print(month_conversions.keys())                         # 遍历所有key
print(month_conversions.values())                       # 遍历所有value

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],          # 利用列表的嵌套使用来实现一个key对应多个value
}
```
### while语句
```
number = input("enter a number: ")
while True:
    if number == "0":
        break                               # break退出循环
    else:
        print(number)
```
```
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue                            # continue返回到循环开头
    print(current_number)                   # 输出1 3 5 7 9
```
### 函数function
```
def pet(type, name):
    print("My " + type + "'s name is " + name.title() + ".")

pet("dog", "harry")                             # 传递位置实参 必须一一对应
pet(name="harry", type="dog")                   # 传递关键字实参 无需一一对应
```
```
# 传递任意数量的实参
def pizza(*toppings)                            # 创建一个名为toppings的空元组
def files(**info)                               # 创建一个名为info的空字典
```
```
# 导入别的模块中的函数的几种方法
import module_name                              # 导入模块
module_name.function_name()                     # 调用模块中的函数

from module_name import function_name           # 导入模块中的函数
function_name()                                 # 调用函数

from module_name import function_name as fn     # 导入模块中的函数并重命名为fn
fn()                                            # 调用函数

import module_name as mn                        # 导入模块并重命名为mn
mn.function_name()                              # 调用模块中的函数

from module_name import *                       # 导入模块中的所有函数
```
