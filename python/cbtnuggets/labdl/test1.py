
#	Project Name	:	Visual Tkinter Python IDE for 2.6
#	Project Date	:	13-12-2009
#	Author		:	livetogogo
#	Contact		:	livetogogo@gmail.com
#	Web			:	http://www.blendertr.org

#!/usr/bin/env python
#-*- coding:utf-8-*-

from tkinter import *


# Do not change. You may experience problems with the design file. #
MainWindow=Tk()
MainWindow.title("Form 1")
MainWindow.resizable(width=FALSE, height=FALSE)
MainWindow.geometry("200x207+250+120")

"""TODO: Place code here."""
#Begin

#End


# Do not change. You may experience problems with the design file. #
Button1=Button(text="Button1", command=Button1Click)
Button1.place(relx=0.12, rely=0.09, relwidth=0.705, relheight=0.175)
def Button1Click():
	showinfo("Visual Tkinter", "I Button 1")
Button1(text = 'Hi there')
MainWindow.mainloop()