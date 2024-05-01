# PDF2Image

简易版pdf2image:

+ 使用[pdf2image](https://pypi.org/project/pdf2image/)模块 (converts a PDF to a PIL object)
+ 将转换结果保存至【以当前为后缀的】文件夹中
+ 图片格式为000~999为索引的png格式图片（可自行修改）

```
images = convert_from_path(str(e1.get()))
if(len(images) > 0):
	cur_time = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
	output_dir = "./output_" + cur_time
	os.mkdir(output_dir)

	for i, img in enumerate(images):
		image_name = os.path.join(output_dir, "{:0>3}.png".format(i))
		img.save(image_name, format='PNG')
```

How to run: `python pdf2image_gui.py`



参考资料：[Convert PDF to Image using Python - GeeksforGeeks](https://www.geeksforgeeks.org/convert-pdf-to-image-using-python/)