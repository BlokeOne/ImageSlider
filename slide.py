import Tkinter as tk

LARGE_FONT = ("Verdana", 12)

class slideshow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames= {}

        for F in (StartPage, ImagePane):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #this start page will take the input from the user
        #have a browse button, and a load button.
        #once load it hit, it will move on to the ImagePane panel.
        label = tk.Label(self, text="Load your pictures", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        labelinput = tk.Label(self, text="Image Folder", font=LARGE_FONT)
        labelinput.pack(pady=20, padx=20)
        inputbox = tk.Entry(self)
        inputbox.pack()
        #lambda is used for sending parameters through on button click
        button1 = tk.Button(self, text="Load",
                            command=lambda: controller.show_frame(ImagePane))
        button1.pack()

class ImagePane(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Image Pane", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        previousbutton = tk.Button(self, text="Previous")
        previousbutton.pack()
        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = slideshow()
app.mainloop()
