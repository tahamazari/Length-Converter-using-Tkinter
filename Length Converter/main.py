from tkinter import *
import tkinter as tk

LARGE_FONT= ("Verdana", 12)   #variable used for setting font

class LengthConverter(tk.Tk):     #main class, used for displaying all frames
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

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
        label = tk.Label(self, text="Welcome to Length Converter", font=('Verdana 18 bold'))
        label.grid(row=1,column=2, padx=(140,20),pady=(15, 30))

        button1 = tk.Button(self, text="Convert Miles",
                            command=lambda: controller.show_frame(PageOne))
        button1.grid(row=4,column=2, padx=(20,20),pady=(15, 30), ipadx=(10))

        button2 = tk.Button(self, text="Convert KM",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=4,column=2, padx=(240,20),pady=(15, 30), ipadx=(10))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Convert From Miles", font=('Verdana 18 bold'))
        label.grid(row=0,column=3, padx=(20,20),pady=(15, 30))


        #functions for converting from miles
        def km2mile():
            print(e1_value.get())
            miles =  float(e1_value.get())*1.609
            t1.insert(END, miles)

        def yard2mile():
            print(e1_value.get())
            km = float(e1_value.get())*1760
            t1.insert(END, km)

        def nm2mile():
            print(e1_value.get())
            nm = float(e1_value.get())*0.868
            t1.insert(END, nm)

        def m2mile():
            print(e1_value.get())
            metre = float(e1_value.get())*1609
            t1.insert(END, metre)

        def feet2mile():
            print(e1_value.get())
            feet = float(e1_value.get())*5280
            t1.insert(END, feet)

        def inch2mile():
            print(e1_value.get())
            inch = float(e1_value.get())*63360
            t1.insert(END, inch)


        #Buttons for converting
        b1 = tk.Button(self, text="Miles to KM", command=km2mile)
        b1.grid(row=5, column=2,pady=(20,0),ipadx=(20))

        b2 = tk.Button(self, text="Miles to Yards", command=yard2mile)
        b2.grid(row=5, column=3,pady=(20,0),ipadx=(20))

        b3 = tk.Button(self, text="Miles to Nautical Miles", command=nm2mile)
        b3.grid(row=5, column=4,pady=(20,0),padx=(0,50),ipadx=(20))

        b4 = tk.Button(self, text="Miles to Metres", command=m2mile)
        b4.grid(row=6, column=2,pady=(20,0),ipadx=(20))

        b5 = tk.Button(self, text="Miles to Feet", command=feet2mile)
        b5.grid(row=6, column=3,pady=(20,0),ipadx=(20))

        b6 = tk.Button(self, text="Miles to Inches", command=inch2mile)
        b6.grid(row=6, column=4,pady=(20,0), padx=(0, 40),ipadx=(20))

        #clearing value
        tclear = tk.Button(self, text="Clear", width=8, command=lambda: t1.delete(1.0,END))
        tclear.grid(row=1, column=4)

        #variable that gets value from entry is e1_value
        e1_value = tk.StringVar()
        e1 = Entry(self, textvariable=e1_value)
        e1.grid(row=1, column=2, padx=(30, 0))

        t1 = tk.Text(self, height=1, width= 15)
        t1.grid(row=1, column=3)



        button1 = tk.Button(self, text="Back to Home", font=('14'),
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=4, pady=(50,20), padx=(0, 10))


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Convert from KM", font=('Verdana 18 bold'))
        label.grid(row=0,column=3, padx=(20,20),pady=(15, 30))


        #function for converting from km
        def mile2km():
            print(e1_value.get())
            miles =  float(e1_value.get())*0.621
            t1.insert(END, miles)

        def yard2km():
            print(e1_value.get())
            km = float(e1_value.get())*1093.61
            t1.insert(END, km)

        def nm2km():
            print(e1_value.get())
            nm = float(e1_value.get())*0.54
            t1.insert(END, nm)

        def m2km():
            print(e1_value.get())
            metre = float(e1_value.get())*1000
            t1.insert(END, metre)

        def feet2km():
            print(e1_value.get())
            feet = float(e1_value.get())*3280.84
            t1.insert(END, feet)

        def inch2km():
            print(e1_value.get())
            inch = float(e1_value.get())*39370.1
            t1.insert(END, inch)

        #Buttons for converting
        b1 = tk.Button(self, text="KM to Miles", command=mile2km)
        b1.grid(row=5, column=2,pady=(20,0),ipadx=(20)) #######

        b2 = tk.Button(self, text="KM to Yards", command=yard2km)
        b2.grid(row=5, column=3,pady=(20,0),ipadx=(20))

        b3 = tk.Button(self, text="KM to Nautical Miles", command=nm2km)
        b3.grid(row=5, column=4,pady=(20,0),padx=(0,50),ipadx=(20))

        b4 = tk.Button(self, text="KM to Metres", command=m2km)
        b4.grid(row=6, column=2,pady=(20,0),ipadx=(20))

        b5 = tk.Button(self, text="KM to Feet", command=feet2km)
        b5.grid(row=6, column=3,pady=(20,0),ipadx=(20))

        b6 = tk.Button(self, text="KM to Inches", command=inch2km)
        b6.grid(row=6, column=4,pady=(20,0), padx=(0, 40),ipadx=(20))

        #for clearing value
        tclear = tk.Button(self, text="Clear", width=8, command=lambda: t1.delete(1.0,END))
        tclear.grid(row=1, column=4)

        #variable that gets value from entry is e1_value
        e1_value = tk.StringVar()
        e1 = Entry(self, textvariable=e1_value)
        e1.grid(row=1, column=2, padx=(30, 0))

        t1 = tk.Text(self, height=1, width= 15)
        t1.grid(row=1, column=3)



        button1 = tk.Button(self, text="Back to Home", font=('14'),
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=4, pady=(50,20), padx=(0, 10))




app = LengthConverter()
app.mainloop()
