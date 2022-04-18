import os,sys
path='/Users/yangshuang/Desktop/3000_dataset1/VOCdevkit/VOC2007/JPEGImages'
filelist=os.listdir(path)
count=len(filelist)
# train_list=filelist[:int(count*0.9)]
# val_list=filelist[int(count*0.9):]


with open("train.txt","w") as f:
    with open('val.txt','w') as f1:
        for i in range(len(filelist)):
            filename=filelist[i].split('.')[0]#0代表取.前面的部分
            x=filelist[i].split('.')[1]
            if x=='jpg':
                if filename[0]!='V':
                    f.write(filename+'\n')
                else:
                    f1.write(filename+'\n')
            else:
                print(filelist[i])

