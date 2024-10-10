from tkinter import *

class MyWindow:
    def close(self):
        window.destroy()

    def Add(self):
        num1 = int(self.entry1.get())
        num2 = int(self.entry2.get())
        result = num1 + num2
        self.result.config(text=str(result))

    def Subtract(self):
        num1 = int(self.entry1.get())
        num2 = int(self.entry2.get())
        result = num1 - num2
        self.result.config(text=str(result))

    def Multiply(self):
        num1 = int(self.entry1.get())
        num2 = int(self.entry2.get())
        result = num1 * num2
        self.result.config(text=str(result))

    def Divide(self):
        num1 = int(self.entry1.get())
        num2 = int(self.entry2.get())
        if num2 != 0:
            result = num1 / num2
            self.result.config(text=str(result))
        else:
            self.result.config(text="Error: Div by 0")

    def Clear(self):
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.result.config(text="")

    def __init__(self, window):
        self.lbl0 = Label(window, text="-----Simple Calculator-----", fg="Purple", font=("Times New Roman", 30))
        self.lbl0.place(x=50, y=0)

        self.lbl1 = Label(window, text="Number 1: ", fg="Orange", font=("Arial Narrow", 25))
        self.lbl1.place(x=50, y=50)
        self.entry1 = Entry(window, font=("Arial Narrow", 25))
        self.entry1.place(x=200, y=50)

        self.lbl2 = Label(window, text="Number 2: ", fg="Orange", font=("Arial Narrow", 25))
        self.lbl2.place(x=50, y=100)
        self.entry2 = Entry(window, font=("Arial Narrow", 25))
        self.entry2.place(x=200, y=100)

        self.lbl3 = Label(window, text="Result: ", fg="Orange", font=("Arial Narrow", 25))
        self.lbl3.place(x=50, y=150)

        self.result = Label(window, text="", fg="Black", font=("Arial Narrow", 25))
        self.result.place(x=200, y=150)

        self.add_button = Button(window, text="Add", font=("Times New Roman", 20), command=self.Add)
        self.add_button.place(x=50, y=200, width=100, height=40)

        self.subtract_button = Button(window, text="Subtract", font=("Times New Roman", 20), command=self.Subtract)
        self.subtract_button.place(x=160, y=200, width=100, height=40)

        self.multiply_button = Button(window, text="Multiply", font=("Times New Roman", 20), command=self.Multiply)
        self.multiply_button.place(x=270, y=200, width=100, height=40)

        self.divide_button = Button(window, text="Divide", font=("Times New Roman", 20), command=self.Divide)
        self.divide_button.place(x=380, y=200, width=100, height=40)

        self.clear_button = Button(window, text="Clear", font=("Times New Roman", 20), command=self.Clear)
        self.clear_button.place(x=490, y=200, width=100, height=40)

        self.exit_button = Button(window, text="Exit", font=("Times New Roman", 30), command=window.destroy)
        self.exit_button.place(x=200, y=300, height=50, width=200)

window = Tk()
window.title("Simple Calculator")
mywindow = MyWindow(window)
window.geometry("630x400")
window.mainloop()
