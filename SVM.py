import cv2
import random
import numpy as np

feature_path = "feature.txt"

#1.read data
all_data = []
all_label = []

fr_read = open(feature_path)
lines = fr_read.readlines()
size = len(lines)
ft_num = 0

for line in lines:
	line = line.strip()
	sp = line.split(' ')
	ft_num = len(sp)-1
	tmp = []
	for i in range(0,ft_num):
		tmp.append(sp[i])
	all_data.append(tmp)
	all_label.append(sp[-1])

print("all data sample: %d" %(len(all_data)))
print(size,ft_num)
print("all label: %d" % (len(all_label)))

#2.shuffle the data
shuffled =  [i for i in range(size)]
random.shuffle(shuffled)
shuffle_data = []
shuffle_label = []

idx = 0
for i in range(0,size):
	idx = shuffled[i]
	shuffle_data.append(all_data[idx][:])
	shuffle_label.append(all_label[idx])

#3.train svm and evaluate function
train_data = []
train_label = []
val_data = []
val_label = []
def Score(svm,paras):
	K = 8      #K-cross validation
	train_size = size/8*7
	val_size = size/8
	score = 0.0
	print("train_size is %d, val_size is %d" % (train_size,val_size))
	for i in range(0,8):             #seperate data
		train_data = []
		train_label = []
		val_data = []
		val_label = []
		st = i*val_size
		for j in range(0,st):
			train_data.append(shuffle_data[j][:])
			train_label.append(shuffle_label[j])
		for j in range(st,st+val_size):
			val_data.append(shuffle_data[j][:])
			val_label.append(shuffle_label[j][:])
		for j in range(st+val_size,size):
			train_data.append(shuffle_data[j][:])
			train_label.append(shuffle_label[j])
		print("train_size is %d, val_size is %d" % (len(train_data),len(val_data)))
		train_x = np.array(train_data,dtype = np.float32)
		train_y = np.array(train_label,dtype = np.float32)
		val_x = np.array(val_data,dtype = np.float32)
		val_label = np.array(val_label,dtype = np.float32)
		print("svm training")
		svm.train(train_x,train_y,params = paras)
		print("svm train finish")
		print(val_x.shape)
		cnt = 0
		for j in range(0,val_x.shape[0]):
			pred = svm.predict(val_x[j]) 
			if(pred == val_label[j]):
				cnt += 1
		print("predict correct %d times" % (cnt))
		score += float(cnt)/val_size
	score = score/K
	return score

'''
C = 5
gamma = 2
svm_params = dict(kernel_type = cv2.SVM_LINEAR,svm_type = cv2.SVM_C_SVC,
			C=C, gamma = gamma)
svm = cv2.SVM()
s = Score(svm,svm_params)
print("C = %d ,gamma = %d, score = %f" % (C,gamma,s))
'''
C_grid = [i for i in range(1,10)]
gamma_grid = [i for i in range(1,10)]
max_score = 0
best_C, best_g = 0, 0

for C in C_grid:
	for gamma in gamma_grid:
		svm_params = dict(kernel_type = cv2.SVM_LINEAR,svm_type = cv2.SVM_C_SVC,
			C=C, gamma = gamma)
		svm = cv2.SVM()
		s = Score(svm,svm_params)
		print("C = %d ,gamma = %d, score = %f" % (C,gamma,s))
		if(s>max_score):
			max_score = s
			best_C = C
			best_g = gamma

print("Best perfomance:\nC = %d ,gamma = %d, score = %f" % (C,gamma,s))



