#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------
#放大一个图层上的像素并放到新建图层上
#放大标准 是增大几圈
#                 。。   。。。   。。。。
#            。-》。。-》。。。-》。。。。
#                        。。。   。。。。
#                                 。。。。
#-------------------------------------------------------------
from gimpfu import *

def enlarge_pxs(image, layer,t_num):
	'''
	Parameters:
		image : image The current image.
		layer : layer The layer of the image that is selected.
		t_num : enlarge num
	'''
	gimp.message(t_num)

register(
	"python_fu_zwd_enlarge_pxs",
	"放大像素",
	"在新图层上放大原图层所有像素",
	"zwd",
	"Open source (BSD 3-clause license)",
	"2013",
	"<Image>/Filters/zwd/enlarge pxs",
	"*",
	[
		(PF_STRING, "t_num", "只能输入整数",2)
	],
	[],
	enlarge_pxs
)

main()
