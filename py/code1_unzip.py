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
    len_ = int(arr/2)
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