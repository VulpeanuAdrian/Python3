from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib
from matplotlib import style
matplotlib.use("TkAgg")
LARGE_FONT = ("Verdana", 12)


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, "images2.ico")
        tk.Tk.wm_title(self, "Function Generator")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (FunctionGeneration, Variants, PageTwo, PageThree):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(FunctionGeneration)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class FunctionGeneration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Function Generator",
                             command=lambda: controller.show_frame(Variants))
        button1.place(relx=0.01, rely=0.08, relwidth=0.2, relheight=0.1)
        # button1.pack()

        button2 = ttk.Button(self, text="Variants",
                             command=lambda: controller.show_frame(PageTwo))
        button2.place(relx=0.01, rely=0.16, relwidth=0.2, relheight=0.1)

        # button2.pack()

        button3 = ttk.Button(self, text="Kmatrix",
                             command=lambda: controller.show_frame(PageThree))
        button3.place(relx=0.01, rely=0.24, relwidth=0.2, relheight=0.1)

        # button3.pack()


class Variants(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Variants", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back To home",
                             command=lambda: controller.show_frame(FunctionGeneration))

        button1.pack()

        button2 = ttk.Button(self, text="Page two",
                             command=lambda: controller.show_frame(PageTwo))

        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back To home",
                             command=lambda: controller.show_frame(FunctionGeneration))

        button1.pack()

        button2 = ttk.Button(self, text="Back To Page one",
                             command=lambda: controller.show_frame(Variants))

        button2.pack()


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back To home",
                             command=lambda: controller.show_frame(FunctionGeneration))

        button1.pack()

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 8, 2, 4, 9, 10])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = MainApp()
app.mainloop()
