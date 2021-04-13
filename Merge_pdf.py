from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox as mbox, font
from PyPDF2 import PdfFileMerger

import os
root = Tk()

wid = root.winfo_screenwidth()
hyt = root.winfo_screenheight()
root.title("PDF MERGE")
w_default = 300
h_default = 300
x = (root.winfo_screenwidth()//2) - int(w_default // 2)
y = (root.winfo_screenheight()//2) - int(h_default//1.7)
# root.resizable(width=FALSE, height=FALSE)
root.geometry(f'{w_default}x{h_default}+{x}+{y}')


files=[]


class MyDialog:

    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        top.geometry(f'{w_default}x{h_default}+{x}+{y}')
        self.myLabel = tk.Label(top, text='Enter Merged PDF Name below')
        self.myLabel.pack()
        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()
        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        self.final_name = self.myEntryBox.get()
        self.top.destroy()

def onClick():
    inputDialog = MyDialog(root)
    root.wait_window(inputDialog.top)
    return inputDialog.final_name

def merge_files():
    try:
        pdfs = files
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)

        merged_name = onClick()
        name = os.path.dirname(files[0]) +"/"+ merged_name+".pdf"
        merger.write(name)
        merger.close()
        mbox.showinfo(title="Saved",message=f'Successfully Merged And Saved As {name}')
    except Exception as e:
        mbox.showinfo(title="Error Occured",message=f"{e}")


def choose_files(listbox):
    global files
    filetype = [("PDF FILES",".pdf")]
    filenames = filedialog.askopenfilenames(filetypes = filetype)
    if len(filenames) > 1:

        try:
            listbox.delete(0,'end')
        except Exception as e:
            print(e)

        files = list(filenames)
        for idx,val in enumerate(files):
            listbox.insert(idx,os.path.basename(val))
            root.update()

    else:
        mbox.showerror(title=" INPUT ERROR ",message="PLEASE SELECT ATLEAST 2 FILES")
    

def main(root):
    main_frame = Frame(root,bg="#bbbbbb")
    main_frame.pack()

    listbox = Listbox(main_frame,bd=5,bg="#fdffbc",relief="solid",width=50,height=10)

    button1 = Button(main_frame,text="Choose Files",bd=5,bg="#bedbbb",relief="solid",width=30,height=3,
    command=lambda: choose_files(listbox))    
    button1.pack()
    listbox.pack()

    button2 = Button(main_frame,text="Merge Files",bd=5,bg="#ffc93c",relief="solid",width=30,height=3,command=lambda: merge_files())    
    button2.pack()

    
if __name__ == "__main__":
    main(root)
    root.mainloop()