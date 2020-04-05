# FirstButtons.py
# First Use of Buttons in GUI

from tkinter import *

# create the root window
root = Tk()
root.title("FirstButtons")
root.geometry("200x85")

# create a frame in the window to hold widgets
app = Frame(root)
app.grid()

# create button for frame
b1 = Button(app, text = "I am useless!")
b1.grid()

b2 = Button(app)
b2.grid()

# created button 2 without text, we can alter the text later with
b2.configure(text = "I also do nothing!")

# create a third button
b3 = Button(app)
b3.grid()
b3["text"] = "Wow! Im not unique"

# start main loop
root.mainloop()