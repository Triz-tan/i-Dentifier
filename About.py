import customtkinter as ctk
import style_register as style
from PIL import Image, ImageTk
import About

class about_window(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1024x600")
        self.title("About Us")
        self.attributes('-topmost', True)
        self.attributes('-fullscreen', True)

        # Load the image file
        self.image = Image.open("/home/identifier/thesis/GUI_images/AboutusBackground.png")

        # Create a PhotoImage object from the image
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas widget with the background image
        self.canvas = ctk.CTkCanvas(self, width=self.image.width, height=self.image.height)
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.photo)
        self.canvas.pack()

        self.back_btn = style.back_btn_style(self, 'Back', self.back_func_btn)
        self.back_btn.place(x=1128.7, y=673.9)



    def back_func_btn(self):
        self.destroy()
        print("Back button just clicked")