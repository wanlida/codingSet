### 题目详细信息  

![image](https://github.com/wanlida/codingSet/raw/master/pictures/code1.png)  

### 代码  

```
def unzip(the_string):
    import numpy as np
    #同时对‘值’和‘字母’进行冒泡排序
    def sort(str):
        length = int(len(str)/2)
		#字符串转化为list数组
        arr = list(str)
		#冒泡排序
        for k in np.arange(length):
            for m in np.arange(length-k+1):
				#list防止访问超出范围
                if (2*m+3)<(2*length) and (2*m+1)<(2*length):
					#如果数字比后面的大，交换位置
                    if arr[2*m+1]>arr[2*m+3]:

                            the_num=arr[2*m+1]
                            arr[2*m+1]=arr[2*m+3]
                            arr[2*m+3]=the_num
                            the_num=None

                            the_str=arr[2*m]
                            arr[2*m]=arr[2*m+2]
                            arr[2*m+2]=the_str                    
                            the_str=None
					#如果 数字等于后面的数字 且 字母比后面的小 ，交换位置		
                    if (arr[2*m+1]==arr[2*m+3]) and ((arr[2*m])<(arr[2*m+2])):
                            the_num=arr[2*m+1]
                            arr[2*m+1]=arr[2*m+3]
                            arr[2*m+3]=the_num
                            the_num=None

                            the_str=arr[2*m]
                            arr[2*m]=arr[2*m+2]
                            arr[2*m+2]=the_str                    
                            the_str=None
		#把list转化为字符串
        return ''.join(arr)
    print(sort("the_string"))  
    list_ = list(sort("v5c4a3b2c5v1m2"))
    print(list_)
    # i=0
    # ord(arr[2*i+1])-48
    arr = len(list_)
    len_ = arr//2 #arr除以2的整数部分
    result=[]
    for i in np.arange(len_):
		#list防止访问超出范围
        if(2*i+1)<arr:
		# ord(list_[2*i+1])-48 能将字符转化为数字 '2' -> 2
            for j in np.arange(ord(list_[2*i+1])-48):
			#通过list.append添加到result 的list
                result.append(list_[2*i])
#把list转化为字符串
    return ''.join(result)                    
#测试结果是否正确
#v5c4a3b2c5v1m2
print(unzip('v5c4a3b2c5v1m2'))
```

### 几个非常重要的函数
```
# -*- coding:utf-8 -*-

str = '3.0.31'

list = str.split('.')

print list

list.append('6789')

print list

var = '.'.join(list)

print var
```
结果
```
['3', '0', '31']
['3', '0', '31', '6789']
3.0.31.6789
```
### python中的字符数字之间的转换函数
```
int(x [,base ])         将x转换为一个整数    
long(x [,base ])        将x转换为一个长整数    
float(x )               将x转换到一个浮点数    
complex(real [,imag ])  创建一个复数    
str(x )                 将对象 x 转换为字符串    
repr(x )                将对象 x 转换为表达式字符串    
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象    
tuple(s )               将序列 s 转换为一个元组    
list(s )                将序列 s 转换为一个列表    
chr(x )                 将一个整数转换为一个字符    
unichr(x )              将一个整数转换为Unicode字符    
ord(x )                 将一个字符转换为它的整数值    
hex(x )                 将一个整数转换为一个十六进制字符串    
oct(x )                 将一个整数转换为一个八进制字符串   

chr(65)='A'
ord('A')=65
 
int('2')=2;
str(2)='2'

```
### 实际上面的代码有点小问题
```
#修正版代码
ord('2')-48 #结果是数字2
```
