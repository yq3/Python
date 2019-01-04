# Python Learning Record
基础知识小结（来源于Mike Dane's Giraffe Academy 以及 Eric Matthes: Python Crash Course）  
### 变量的命名和使用  
* 变量名只能包含字母、数字和下划线，可以字母或下划线打头，但不能以数字打头
* 慎用小写字母l和大写字母O，可能会被误认为数字1和0
### 关于字符串
```
name.title()            #首字母大写
name.upper()            #全部大写
name.lower()            #全部小写
name.isupper()          #判别是否是大写
len(name)               #字符串的长度
print(name[0])          #按位显示
name.strip()            #剔除字符串两端的空白
```
制表符\t  
换行符\n  
### 关于数字
```
print(10 % 3)                  #取余
print(3 ** 3)                  #乘方
my_num = 5
print(str(my_num) + " apples")
print(abs(my_num))             #绝对值
print(pow(3, 2))               #幂
print(max(3, 2))               #取大值
print(round(3.7))              #四舍五入
from math import *
print(floor(3.7))              #舍去小数
print(ceil(3.2))               #有小数便加一
print(sqrt(9))                 #开方根

num1 = input("enter a number: ")      # Building a Basic Calculator
num2 = input("enter another number: ")
result = float(num1) + float(num2)
print(result)
```
### 关于列表
```
friends = ["Jack", "Kim", "Amy", "Mike", "Bob"]
numbers = [2, 4, 6]   
friends[1] = "Carl"                 #修改第二个元素
print(friends[0])                   #第一个
print(friends[-1])                  #倒数第一个
print(friends[-2])                  #倒数第二个
print(friends[1:])                  #从1往后
print(friends[1:3])                 #从1到3不包括3              
friends.extend(numbers)             #把两个list加到一起
friends.append("Dave")              #添加一个元素到末尾
friends.insert(1, "Ellen")          #添加一个元素到某一位置 原始元素将被右移
del friends[0]                      #移除某元素
friends.remove("Bob")               #移除某元素
friends.clear()                     #清除列表
friends.pop()                       #弹出（清除）最后一个元素 弹出的元素可被使用
friends.pop(0)                      #弹出指定的一个元素
print(friends.index("Mike"))        #检测MIke是否在list里面
print(friends.count("Mike"))        #mike在list里面出现了几次
friends.sort()                      #按字母顺序排序
friends.sort(reverse=True)          #按字母顺序的相反顺序排序
friends.sorted()                    #暂时按字母顺序排序
numbers.sort()                      #按升序排序
numbers.reverse()                   #颠倒顺序（与原顺序相比）
friends2 = friends.copy()           #复制list
```
