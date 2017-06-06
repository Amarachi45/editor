import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

top = Tkinter.Tk(className="Text Pad")
#create text area
textPad = ScrolledText(top, width=100, height=80)

# create a menu & define functions for each menu item

def open_command():
    file = tkFileDialog.askopenfile(parent=top,mode='rb',title='Select a file')
    if file != None:
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

def save_command(self):
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
        data = self.textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Another TextPad \n Copyright \n No rights left to reserve")

def new():
    print "I am a new Command"
menu = Menu(top)
top.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

textPad.pack()
top.mainloop()
