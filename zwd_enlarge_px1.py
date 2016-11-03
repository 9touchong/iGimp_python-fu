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
	# Get the layer position.
	pos = 0;
	for i in range(len(image.layers)):
		if(image.layers[i] == layer):
			pos = i
	# Create a new layer to save the results
	newLayer = gimp.Layer(image, layer.name + "_"+str(t_num)+"enlarge", layer.width*t_num, layer.height*t_num, layer.type, layer.opacity, layer.mode)
	image.add_layer(newLayer, pos)
	gimp.message("输入的是"+str(t_num))

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
		(PF_INT8, "t_num", "只能输入整数",2)
	],
	[],
	enlarge_pxs
)

main()
