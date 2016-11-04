# iGimp_python-fu
仅作脚本保存备份，用于gimp的python脚本试验
此目录下进行一点gimp的python-fu的试验学习
会有一些脚本和图像文件
python-fu用的是python2
#
py脚本要拷贝到/home/user/.gimp-2.8/plug-ins下(win不是，可参考首选项找到具体位置)并更改权限(不必root这里直接chmod 777了事)才能运行
有时无法运行 可查看是否是中文问题
#
zwd_enlarge_px1.py 在图像较小且简单情况可以实现功能 但算法是最笨的 速度慢到吓人 稍复杂图像就
会丢失部分像素
zwd_enlarge_px2.py 在zwd_enlarge_px1.py基础上主要进行速度方向的优化 就是添加了if pixel[3]=="\x00":continue来跳过空像素的新图层处理
