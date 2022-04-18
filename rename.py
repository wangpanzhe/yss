

import shutil
import re
import sys
import os
#这个库复制文件比较省事

def objFileName():
    '''
    生成文件名列表
    :return:
    '''
    path_img=sys.path[0]+"/imgs/"
    path_mask=sys.path[0]+"/mask/"
    fileList_img = os.listdir(path_img)
    fileList_mask=os.listdir(path_mask)
    obj_name_list = []
    index =0
    for filename in fileList_img:
        i=fileList_mask.index(filename) if(filename in fileList_mask) else -1
        if i != -1:
            oldname=path_img+os.sep+filename
            newname=path_img+os.sep+str(index)+os.path.splitext(filename)[1]
            os.rename(oldname,newname)
            oldname=path_mask+os.sep+filename
            newname=path_mask+os.sep+str(index)+os.path.splitext(filename)[1]
            os.rename(oldname,newname)
            obj_name_list.append(str(index))
        
        index=index+1
    return obj_name_list

def copy_img():
    '''
    复制、重命名、粘贴文件
    :return:
    '''
    local_img_name=sys.path[0]+'/yaml/abc.yaml'
    #指定要复制的图片
    cppath = sys.path[0]+'/yaml'
    #指定存放图片的目录
    for i in objFileName():
        new_obj_name = i+'.yaml'
        shutil.copy(local_img_name,cppath+'/'+new_obj_name)

if __name__ == '__main__':
    copy_img()