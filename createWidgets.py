from tkinter import *

def createLabel(root, text):
    width = max([30,len(str(text))])
    label = Label(master=root,
                  text=text,
                  width=width,
                  anchor=W,
                  justify=LEFT,
                  bg='gold')
    return label

def createEntry(root, show=None):
    if show == None:
        show = ''
    entry = Entry(master=root,
                  show=show,
                  width=30)
    return entry

def createButton(root, text, command, bg=None):
    if bg == None:
        bg = 'blue'
    button = Button(master=root,
                    text=text,
                    command=command,
                    height=3,
                    width=30,
                    bg=bg,
                    fg='white')
    return button
