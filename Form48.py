import customtkinter as ctk
import style_register as style
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess

# Define a class named 'form48' that inherits from 'ctk.CTkToplevel'
class form48(ctk.CTkToplevel):
    
    def __init__(self, master):
        super().__init__(master)

        self.geometry("1366x768")
        self.title("Register")
        self.attributes('-topmost', True)
        self.attributes('-fullscreen', True)

        # Load the image file
        self.image = Image.open("GUI_images/CSCFORM48.png")

        # Create a PhotoImage object from the image
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas widget with the background image
        self.canvas = ctk.CTkCanvas(self, width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.photo)
        self.canvas.pack()
        
        # Create username and password entry fields with style
        self.username = style.entry_style_csc(self, "Enter your username")
        self.username.place(x=778, y=282.7)

        self.password = style.entry_style_csc(self, "Enter your password")
        self.password.place(x=778, y=396.2)

        # Create login button with style and bind it to login_func_btn method
        self.login_btn = style.login_btn_style(self, "Login", self.login_func_btn)
        self.login_btn.place(x=863.2, y=477.8)

        # Create back button with style and bind it to back_func_btn method
        self.back_btn = style.back_btn_style(self, 'Back', self.back_func_btn)
        self.back_btn.place(x=1122.5, y=652.4)

        # Define dictionary of valid usernames and passwords
        self.users = {
            'admin': 'admin',
            'pupbinan': 'identifier',
        }

    # Method to handle login button click
    def login_func_btn(self):
        print("Log in button just click")
        # Get the user's input from the entry widgets
        username = self.username.get()
        password = self.password.get()

        # Validate the user's credentials
        if username in self.users and self.users[username] == password:
            self.attributes('-topmost', False)
            messagebox.showinfo('Success', 'Login successful!')
            self.attributes('-topmost', True)

            self.master.attributes('-topmost', False)
            # Open Csc_Form_48.xlsx file using LibreOffice Calc
            subprocess.run(["libreoffice", "--calc", "Csc_Form_48.xlsx"])
            self.destroy()
        else:
            self.attributes('-topmost', False)
            messagebox.showerror('Error', 'Invalid username or password')
            self.attributes('-topmost', True)
            self.destroy()

    # Method to handle back button click
    def back_func_btn(self):
        self.destroy()
        print("Back button just clicked")

# Create an instance of the 'form48' class and run the application
if __name__ == "__main__":
    app = form48(ctk.CTkToplevel)
    app.mainloop()
