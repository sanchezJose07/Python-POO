import tkinter 
class Interfaz: 
    def __init__ (self, win):
        self.f1 = tkinter.Label(win, text="COLOR",fg="black")
        self.f2 = tkinter.Button(win, text = "AMARILLO",fg="yellow",bg="grey",command=self.TurnYellow)
        self.f3 = tkinter.Button(win,text= "ROJO",fg="red",bg="grey",command=self.TurnRed)
        self.f4 = tkinter.Button(win, text = "BLANCO",fg="white",bg="grey",command=self.TurnWhite)
        self.f1.grid(column=0,row=0,columnspan=8)
        self.f2.grid(column=0,row=8)
        self.f3.grid(column=2,row=8)
        self.f4.grid(column=4,row=8)
        
    def TurnYellow(self):
        cont=window
        self.f1=tkinter.Label(cont,text="COLOR",fg="yellow")
        self.f1.grid(column=0,row=0,columnspan=8)
    def TurnRed(self):
        cont=window
        self.f1=tkinter.Label(cont,text="COLOR",fg="red")
        self.f1.grid(column=0,row=0,columnspan=8)
    def TurnWhite(self):
        cont=window
        self.f1=tkinter.Label(cont,text="COLOR",fg="white")
        self.f1.grid(column=0,row=0,columnspan=8)
        
window = tkinter.Tk()
intfaz = Interfaz(window)
window.mainloop()
