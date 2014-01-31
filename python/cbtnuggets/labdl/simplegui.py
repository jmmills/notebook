from tkinter import *

root = Tk()
root.title('Button App')
Label(text='I am a button').pack(pady = 15)

def quitapp():
    root.destroy()
    
Button(text='Quit', command = quitapp).pack(side=BOTTOM)
root.mainloop()
