# -*- coding:UTF-8 -*-
# 导入数据增强工具
# import Augmentor
# p=Augmentor.Pipeline("/Users/yangshuang/Desktop/dataexpansion/test2")
#
# # 图片逆时针随机旋转90度
# p.rotate90(probability=0.5)
# p.sample(717)
# # 图片顺时针随机旋转90度
# # p.rotate270(probability=0.5)
# # p.sample(717)

import Augmentor

# 确定原始图像存储路径以及掩码文件存储路径
p = Augmentor.Pipeline("/Users/yangshuang/Desktop/expenddata/test1")
p.ground_truth("/Users/yangshuang/Desktop/expenddata/test2")

# # 图像旋转： 按照概率0.6执行，左旋角度20，右旋角度20
# p.rotate(probability=0.6, max_left_rotation=20, max_right_rotation=20)

# 图片逆时针随机旋转90度
p.rotate90(probability=0.5)
# 图片顺时针随机旋转90度
p.rotate270(probability=0.5)

#图像左右翻转： 按照概率0.7执行
p.flip_left_right(probability=0.7)

#图像放大缩小： 按照概率0.6执行，面积为原始图0.8倍
p.zoom_random(probability=0.6, percentage_area=0.8)

# 最终扩充的数据样本数
p.sample(3000)

