import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title("WIKIPEDIA")
win.geometry("260x70")


def search_wiki():
    search = entry.get()
    hasil = wikipedia.summary(search)
    showinfo("Hasil Pencarian", hasil)


label = Label(win, text="Wikipedia Search :")
label.grid(row=0, column=0)

entry = Entry(win)
entry.grid(row=1, column=0)

button = Button(win, text="Search", command=search_wiki)
button.grid(row=1, column=1, padx=10)

win.mainloop()
