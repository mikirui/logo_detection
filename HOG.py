import cv2
import os
import os.path
import shutil

positive_path = "positive2/"
negative_path = "negative2/"
feature_path = "feature2.txt"

fr_w = open(feature_path,"w")
winSize = (40,40)
blockSize = (18,18)
blockStride = (11,11)
cellSize = (6,6)
winstride = (24,4)
nbins = 9

positive = 0
negative = 0
for parent,dirname,filename in os.walk(positive_path):
	for img in filename:
		original_path = os.path.join(parent,img)
		image = cv2.imread(original_path)
		hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
		hist = hog.compute(image,winstride)
		
		print(hist.shape)
		print(original_path)
		res = ""
		for i in range(0,hist.shape[0]):
			res += str(hist[i][0])
			res += ' '
		res += '1\n'
		positive += 1
		fr_w.write(res)


for parent,dirname,filename in os.walk(negative_path):
	for img in filename:
		original_path = os.path.join(parent,img)
		image = cv2.imread(original_path)
		hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
		hist = hog.compute(image,winstride)
		print(original_path)
		res = ""
		for i in range(0,hist.shape[0]):
			res += str(hist[i][0])
			res += ' '
		res += '-1\n'
		negative += 1
		fr_w.write(res)

print("positive sample: %d;\nnegative sample:%d" % (positive,negative))
fr_w.close()


