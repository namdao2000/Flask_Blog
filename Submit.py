from tkinter import *
import os


class Submit(Tk):
    def __init__(self):
        super().__init__()
        self.attributes("-topmost", True)
        self.title("Ez Submit")
        self.geometry("225x50")
        self.label_1 = Label(self, text="Commit Message")
        self.entry_1 = Entry(self)
        self.button1 = Button(self, text="git push", command=self.submit)
        self.label_1.grid(row=0, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.button1.grid(row=1, columnspan=2)

    def submit(self):
        message = self.entry_1.get()
        if message is None:
            message = "Update"
        os.system("git commit -a -m \"{}\" ".format(message))
        os.system("git push")


app = Submit()
app.mainloop()
