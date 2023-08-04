import customtkinter as ctk
import style_register as style
from PIL import Image, ImageTk


class How_it_works(ctk.CTkToplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1366x768")
        self.title("Register")
        self.attributes('-topmost', True)
        self.attributes('-fullscreen', True)

        # Load the image file
        self.image = Image.open("/home/identifier/thesis/GUI_images/Howitworks.png")

        # Create a PhotoImage object from the image
        self.photo = ImageTk.PhotoImage(self.image)

        # Create a canvas widget with the background image
        self.canvas = ctk.CTkCanvas(self, width=self.image.width,   eight=self.image.height)
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=self.photo)
        self.canvas.pack()
        
        self.back_btn = style.back_btn_style(self, 'Back', self.back_func_btn)
        self.back_btn.place(x=1122.5, y=652.4)

    def back_func_btn(self):
        self.destroy()