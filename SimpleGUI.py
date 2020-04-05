# Simple GUI Program
# create a window

from tkinter import *

# create the root window
root = Tk()

# modify the window
root.title("Simple GUI")
root.geometry("1280x720")

# create a frame
app = Frame(root)

app.grid()

# create a label in the frame
lbl = Label(app, text = "I am label, read me")

# invoke the labels grid method
lbl.grid()

# start event loop
root.mainloop()


