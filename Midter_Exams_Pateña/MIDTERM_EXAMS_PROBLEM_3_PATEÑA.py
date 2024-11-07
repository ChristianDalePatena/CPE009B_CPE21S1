import tkinter as tk

class FullNameDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Midterm in OOP")
        self.geometry("450x250")

        self.label = tk.Label(self, text="Enter your fullname:", fg="red")
        self.label.place(x=20, y=50)

        self.name_input = tk.Entry(self, bd = 4)
        self.name_input.place(x=240, y=60, width = 180, height = 30)

        self.button = tk.Button(self, text="Click to display your Fullname", command=self.display_name, fg="red")
        self.button.place(x=20, y=90)

        self.output = tk.Entry(self, bd = 4, state='readonly')
        self.output.place(x=240, y=100, width = 180, height = 30)

    def display_name(self):
        name = self.name_input.get()
        self.output.config(state='normal')
        self.output.delete(0, tk.END)
        self.output.insert(0, name)
        self.output.config(state='readonly')

if __name__ == "__main__":
    app = FullNameDisplayApp()
    app.mainloop()
