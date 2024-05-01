import os
import time
from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox

def pdf2img():
	try:
		images = convert_from_path(str(e1.get()))
		if(len(images) > 0):
			cur_time = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
			# print(cur_time)
			output_dir = "./output_" + cur_time
			os.mkdir(output_dir)

			for i, img in enumerate(images):
				image_name = os.path.join(output_dir, "{:0>3}.png".format(i))
				img.save(image_name, format='PNG')

	except :
		Result = "NO pdf found"
		messagebox.showinfo("Result", Result)

	else:
		Result = "success"
		messagebox.showinfo("Result", Result)


if __name__ == "__main__":
	master = Tk()
	Label(master, text="File Location").grid(row=0, sticky=W) 

	e1 = Entry(master)
	e1.grid(row=0, column=1)

	b = Button(master, text="Convert", command=pdf2img)
	b.grid(row=0, column=2,columnspan=2, rowspan=2,padx=5, pady=5)

	mainloop()
