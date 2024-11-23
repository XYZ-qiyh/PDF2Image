import os
import time
from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def pdf2img():
    try:
        selected_pdf_file = str(e1.get())
        images = convert_from_path(selected_pdf_file)
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


def select_file():
    filetypes = (
        ('text files', '*.pdf'),
    )

    filename = filedialog.askopenfilename(
        title='Open PDF File',
        initialdir='/',
        filetypes=filetypes)

    # messagebox.showinfo(
    #     title='Selected File',
    #     message=filename
    # )
    print("selected file: {}".format(filename))
    e1.delete(0, END)
    e1.insert(0, filename)


if __name__ == "__main__":
    master = Tk()
    master.title('PDF2image')
    Label(master, text="File Location").grid(row=0, sticky=W) 

    e1 = Entry(master)
    e1.grid(row=0, column=1)

    open_button = Button(
        master,
        text='Load File',
        command=select_file
    )
    open_button.grid(row=0, column=2)

    convert_button = Button(
        master,
        text="Convert",
        command=pdf2img
    )
    convert_button.grid(row=0, column=3, padx=5, pady=5)

    mainloop()
