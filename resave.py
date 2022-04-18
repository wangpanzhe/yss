import os
import matplotlib.image as img # img 用于读取图片
import shutil

VOCdevkit_path='VOCdevkit'
with open(os.path.join(VOCdevkit_path, "/Users/yangshuang/Desktop/VOCdevkit/VOC2007/ImageSets/Segmentation/test.txt"),"r") as f:
        val_lines = f.read().splitlines()
print(val_lines)

 
for i in val_lines:
        picture=i+'.jpg'
        local_img_name='/Users/yangshuang/Desktop/VOCdevkit/VOC2007/JPEGImages/'+picture
        copy_img_name='/Users/yangshuang/Desktop/3000_test/3000_test_img/'+picture

        shutil.copy(local_img_name,copy_img_name)
print('success')