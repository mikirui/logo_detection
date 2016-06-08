import os
import os.path
import shutil
from PIL import Image

original_positive = "high/"
other_negative1 = "big/"
other_negative2 = "new/"
positive_path = "positive2/"
negative_path = "negative2/"

os.mkdir(positive_path)
os.mkdir(negative_path)

idx = 1
for parent,dirname,filename in os.walk(original_positive):
	for img in filename:
		original_path = os.path.join(parent,img)
		ext = os.path.splitext(img)[1]     #get extension of filename
		target_path = positive_path + str(idx) + ext       #rename the filename
		idx += 1
		shutil.copy(original_path,target_path)
		img_t = Image.open(target_path)
		img_t = img_t.resize((88,44))
		if(ext == ".jpg"):
			ext = ".jpeg"
		img_t.save(target_path,ext[1:])
		print(original_path + "->" +target_path)


idx = 1
for parent,dirname,filename in os.walk(other_negative1):
	for img in filename:
		original_path = os.path.join(parent,img)
		ext = os.path.splitext(img)[1]     #get extension of filename
		target_path = negative_path + str(idx) + ext       #rename the filename
		idx += 1
		shutil.copy(original_path,target_path)
		img_t = Image.open(target_path)
		img_t = img_t.resize((88,44))
		if(ext == ".jpg"):
			ext = ".jpeg"
		img_t.save(target_path,ext[1:])
		print(original_path + "->" +target_path)


for parent,dirname,filename in os.walk(other_negative2):
	for img in filename:
		original_path = os.path.join(parent,img)
		ext = os.path.splitext(img)[1]     #get extension of filename
		target_path = negative_path + str(idx) + ext       #rename the filename
		idx += 1
		shutil.copy(original_path,target_path)
		img_t = Image.open(target_path)
		img_t = img_t.resize((88,44))
		if(ext == ".jpg"):
			ext = ".jpeg"
		img_t.save(target_path,ext[1:])
		print(original_path + "->" +target_path)

