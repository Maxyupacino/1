import math #引入函数
list1=[]
for i in range(3,10001): #遍历3到10000的所有数
    for j in range(2,int(math.sqrt(i))+2):  #遍历i/2以下的所有数
        if i%j==0:  #如果有能够整除
            break
    else:  #没有能够整除
        list1.append(i)  #将i加入list1
print(list1)  #打印出list1
