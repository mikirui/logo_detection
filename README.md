#logo_detection

#build_dataset.py

将三类logo样本划分为两类，正类和负类，并将图像统一为一定的大小(88*44)

#HOG.py

提取图片的HOG特征写入txt文件

1.共2136个样本，其中正样本693个('最新')，负样本1443个('最大',’最高')

2.每个样本4374个特征，

3.特征格式：

(1)每个样本一行

特征1 特征2 ... 1(或-1)

(2)特征之间是一个空格，最后一个数字1代表正样本，-1代表负样本

#SVM.py

利用opencv封装好的SVM进行训练
