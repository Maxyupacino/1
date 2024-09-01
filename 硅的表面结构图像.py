from pylab import scatter,xlabel,ylabel,xlim,ylim,show,imshow  #引入pylab库的函数
from numpy import loadtxt  #引入numpy库的函数
data1 = loadtxt("stm.txt",float)  #读取txt文档内数据
x=data[:,0]  #确立x的取值，搜索data数据
y=data1[:,1]  #确立y的取值，搜索data数据
scatter(x,y)  #绘画出图像
xlabel("x")
ylabel("y")
imshow(data1)
show()  #显示图像