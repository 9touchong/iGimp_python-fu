#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------
#放大一个图层上的像素并放到新建图层上
#放大标准 是增大几圈
#                 。。   。。。   。。。。
#            。-》。。-》。。。-》。。。。
#                        。。。   。。。。
#                                 。。。。
#在zwd_enlarge_px1.py基础上 些许优化
#-------------------------------------------------------------
# It can be executed by selecting the menu option: 'Filters/zwd/enlarge pxs'
# or by writing the following lines in the Python console (that can be opened with the
# menu option 'Filters/Python-Fu/Console'):
# >>> image = gimp.image_list()[0]
# >>> layer = image.layers[0]
# >>> t_num=2
# >>> gimp.pdb.python_fu_zwd_enlarge_pxs_2(image, layer,t_num)
from gimpfu import *
import datetime

def enlarge_pxs(image, layer,t_num):
	'''
	Parameters:
		image : image The current image.
		layer : layer The layer of the image that is selected.
		t_num : enlarge num
	'''
	t_starttime=datetime.datetime.now()
	# Indicates that the process has started
	gimp.progress_init("enlargeing " + layer.name + "...")
	#Set up an undo group, so the operation will be undone in one step.
	pdb.gimp_image_undo_group_start(image)
	# Get the layer position.
	pos = 0;
	for i in range(len(image.layers)):
		if(image.layers[i] == layer):
			pos = i
	# Create a new layer to save the results
	newLayer = gimp.Layer(image, layer.name + "_"+str(t_num)+"enlarge", layer.width*t_num, layer.height*t_num, layer.type, layer.opacity, layer.mode)
	image.add_layer(newLayer, pos)
	# Clear the new layer.
	pdb.gimp_edit_clear(newLayer)
	newLayer.flush()
	#do
	try:
		# Get the pixel regions.
		srcRgn = layer.get_pixel_rgn(0, 0, layer.width, layer.height, False, False)
		dstRgn = newLayer.get_pixel_rgn(0, 0, newLayer.width, newLayer.height, True, False)
		for x in range(layer.width):
			# Update the progress bar.
			gimp.progress_update(float(x) / float(layer.width))
			for y in range(layer.height):
				pixel = srcRgn[x,y]
				if pixel[3]=="\x00":
					continue
				#Update Update points in dstRgn
				for new_x in range(x*t_num,x*t_num+t_num):
					for new_y in range(y*t_num,y*t_num+t_num):
						dstRgn[new_x,new_y]=pixel
		# Update the new layer.
		newLayer.flush()
		newLayer.merge_shadow(True)
		newLayer.update(0, 0, newLayer.width, newLayer.height)
	except Exception as err:
		gimp.message("Unexpected error: " + str(err))
	# Close the undo group.
	pdb.gimp_image_undo_group_end(image)
	# End progress.
	pdb.gimp_progress_end()
	t_endtime=datetime.datetime.now()
	gimp.message("耗时"+str(t_endtime-t_starttime))

register(
	"python_fu_zwd_enlarge_pxs_2",
	"放大像素",
	"在新图层上放大原图层所有像素",
	"zwd",
	"Open source (BSD 3-clause license)",
	"2013",
	"<Image>/Filters/zwd/enlarge pxs 2",
	"*",
	[
		(PF_INT8, "t_num", "只能输入整数",2)
	],
	[],
	enlarge_pxs
)

main()
