from tkinter import *


# RegistrationForm
class MyWindow:






   def submit(self):
       username = self.entry1.get()
       password = self.entry2.get()
       email = self.entry3.get()
       contacts = self.entry4.get()
       print(f"Username: {username}, Password: {password}, E-Mail: {email}, Contacts: {contacts}")


   def Clear(self):
       self.entry1.delete(0, 'end')
       self.entry2.delete(0, 'end')
       self.entry3.delete(0, 'end')
       self.entry4.delete(0, 'end')
       self.result.config(text="")


   def __init__(self, window):
       self.window = window
       self.window.title("Registration App")
       self.window.geometry("500x500")
       self.window.resizable(False, False)


       self.lbl0 = Label(window, text="-----Account Registration-----", fg="Purple", font=("Times New Roman", 20))
       self.lbl0.pack(pady=10)


       self.lbl1 = Label(window, text="Username: ", fg="Orange", font=("Arial Narrow", 15))
       self.lbl1.pack(pady=(10, 0))
       self.entry1 = Entry(window, font=("Arial Narrow", 15))
       self.entry1.pack(pady=(0, 10))


       self.lbl2 = Label(window, text="Password: ", fg="Orange", font=("Arial Narrow", 15))
       self.lbl2.pack(pady=(10, 0))
       self.entry2 = Entry(window, font=("Arial Narrow", 15), show="*")
       self.entry2.pack(pady=(0, 10))


       self.lbl4 = Label(window, text="E-Mail: ", fg="Orange", font=("Arial Narrow", 15))
       self.lbl4.pack(pady=(10, 0))
       self.entry3 = Entry(window, font=("Arial Narrow", 15))
       self.entry3.pack(pady=(0, 10))


       self.lbl5 = Label(window, text="Contact No.: ", fg="Orange", font=("Arial Narrow", 15))
       self.lbl5.pack(pady=(10, 0))
       self.entry4 = Entry(window, font=("Arial Narrow", 15))
       self.entry4.pack(pady=(0, 10))


       self.submit_button = Button(window, text="Submit", font=("Arial Narrow", 15), command=self.submit)
       self.submit_button.pack(pady=10)


       self.exit_button = Button(window, text="Exit", font=("Arial Narrow", 15), command=window.destroy)
       self.exit_button.pack(pady=5)












window = Tk()
app = MyWindow(window)
window.mainloop()







