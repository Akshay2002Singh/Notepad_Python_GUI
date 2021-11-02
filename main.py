from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.filedialog import askopenfilename ,asksaveasfile
import os


# functions
def newFile():
    global file
    root.title("Ultitled - Notepad")
    file=None
    textarea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*"),("Text Documents","*.txt")])
    if file=="":
        file= None
    else:
        root.title(str(os.path.basename(file))+" - Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file=asksaveasfile(defaultextension=".txt",filetypes=[("All Files","*"),("Text Documents","*.txt")])
        # save as a new file
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" - Notepad")
        print("File Saved")
    else:
        # save the file 
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

def cut():
    textarea.event_generate("<Control-x>")
def copy():
    textarea.event_generate("<Control-c>")
def paste():
    textarea.event_generate("<Control-v>")
def select_all():
    textarea.tag_add(SEL, "1.0", END)
def Theme_dark():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="Black",fg="White")
def Theme_light():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="White",fg="Black")
def light_red():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="White",fg="Red")
def light_green():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="White",fg="Green")
def light_magenta():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="White",fg="Magenta")

def dark_cyan():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="Black",fg="Cyan")
def dark_yellow():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="Black",fg="Yellow")
def dark_red():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="Black",fg="Red")
def dark_green():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="Black",fg="Green")
def dark_magenta():
    textarea.config(font=f"{font.get()} {font_size.get()}",background="Black",fg="Magenta")




def about():
    showinfo("Notepad","Notepad created by Elite for personal use")

if __name__=="__main__":
    root = Tk()
    # window size
    root.title("Elite_notepad")
    root.geometry("900x600")
    root.minsize(900,200)

    # font and fontsize
    font=StringVar()
    font_size=IntVar()
    font.set("Ariel")
    font_size.set(13)


    # text area
    f1=Frame(root)
    f1.pack(side=LEFT,fill=BOTH,expand=True)
    textarea=Text(f1,font=f"{font.get()} {font_size.get()}")
    textarea.pack(expand=True,fill=BOTH)


    file=None


    # main menu
    mainmenu=Menu(root)

    # File menu
    Filemenu=Menu(mainmenu,tearoff=0)
    # create new file
    Filemenu.add_command(label="New",command=newFile)
    # to open a existing file
    Filemenu.add_command(label="Open",command=openFile)
    # save file 
    Filemenu.add_command(label="Save",command=saveFile)
    Filemenu.add_separator()
    Filemenu.add_command(label="Exit",command=quit)
    mainmenu.add_cascade(label="File",menu=Filemenu)
    # edit menu 
    Editmenu=Menu(mainmenu,tearoff=0)
    Editmenu.add_command(label="Cut",command=cut,accelerator='Ctrl+X')
    Editmenu.add_command(label="Copy",command=copy,accelerator='Ctrl+C')
    Editmenu.add_command(label="Paste",command=paste,accelerator='Ctrl+V')
    Editmenu.add_command(label="Select All",command=select_all)
    mainmenu.add_cascade(label="Edit",menu=Editmenu)
    # Theme
    Theme_menu=Menu(mainmenu,tearoff=0)
    Theme_menu.add_command(label="Light",command=Theme_light)
    Theme_menu.add_command(label="Light Red",command=light_red)
    Theme_menu.add_command(label="Light Green",command=light_green)
    Theme_menu.add_command(label="Light Magenta",command=light_magenta)
    Theme_menu.add_command(label="Dark",command=Theme_dark)
    Theme_menu.add_command(label="Dark Cyan",command=dark_cyan)
    Theme_menu.add_command(label="Dark Magenta",command=dark_magenta)
    Theme_menu.add_command(label="Dark Yellow",command=dark_yellow)
    Theme_menu.add_command(label="Dark Red",command=dark_red)
    Theme_menu.add_command(label="Dark Green",command=dark_green)

    mainmenu.add_cascade(label="Theme",menu=Theme_menu)
    


    # help menu 
    helpmenu=Menu(mainmenu,tearoff=0)
    helpmenu.add_command(label="About Notebook",command=about)
    mainmenu.add_cascade(label="Help",menu=helpmenu)
    
    root.config(menu=mainmenu)

    # adding Scrollbar
    Scroll =Scrollbar(root)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()


