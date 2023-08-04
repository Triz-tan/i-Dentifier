#!/usr/bin/env python3

# Import necessary libraries
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

# Import custom style, modules, and classes
import style_register as style
import Face_Recognize
import Register
import About
import Form48
import How

# Set appearance mode to "light"
ctk.set_appearance_mode("light")

# Create the App class
class App:
    def __init__(self):
        # Create the root window
        self.root = ctk.CTk()
        self.root.geometry("1366x768")
        self.root.title('Home')
        self.root.attributes('-fullscreen', True)

        # Load the background image
        self.image = Image.open("GUI_images/HomeBackground.png")
        # Create a PhotoImage object from the image
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas widget with the background image
        self.canvas = ctk.CTkCanvas(self.root, width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.photo)
        self.canvas.pack()

        # Create buttons with styles
        self.register_button = style.btn_style(self.root, 'Register', self.register)
        self.register_button.place(x=870.9, y=41.3)

        self.recognize_button = style.btn_style(self.root, 'Attendance', self.recognize)
        self.recognize_button.place(x=729.6, y=41.3)

        self.dtr_button = style.btn_style(self.root, 'About Us', self.AboutUs)
        self.dtr_button.place(x=1153.1, y=41.3)

        self.about_button = style.btn_style(self.root, 'CSC Form 48', self.form_48)
        self.about_button.place(x=1012, y=41.3)

        self.howitworks_button = style.btn_style_howitworks(self.root, "How It Works", self.howitworks)
        self.howitworks_button.place(x=151.6, y=343.2)

        self.exit_btn = style.exit_btn_style(self.root, 'x', self.exit_btn_func)
        self.exit_btn.place(x=1345, y=744)

    def AboutUs(self):
        # Open About Us window
        About.about_window(self.root).mainloop()

    def register(self):
        # Open Register window
        Register.register_window(self.root).mainloop()

    def recognize(self):
        # Open Face Recognition window
        Face_Recognize.face_recog_window(self.root).mainloop()

    def form_48(self):
        # Open CSC Form 48 window
        Form48.form48(self.root).mainloop()

    def howitworks(self):
        # Open How It Works window
        How.How_it_works(self.root).mainloop()

    def exit_btn_func(self):
        # Destroy the root window and exit the program
        self.root.destroy()
        
# Main entry point of the program
if __name__ == '__main__':
    # Create an instance of the App class and run the tkinter event loop
    app = App()
    app.root.mainloop()
