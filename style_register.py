import customtkinter as ctk
import tkinter as tk

def btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="#464648",
                        hover= True,
                        hover_color= "#5EB4E7",
                        fg_color="#F6F6F6",
                        height= 39.4,
                        width= 136.1,
                        corner_radius=10,
                        border_color= None,
                        bg_color="#F6F6F6"
                        )
    return btn

def btn_style_howitworks(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="#FFFFFF",
                        fg_color="#F7A120",
                        hover= True,
                        hover_color= "#282E2D",
                        height= 39.4,
                        width= 136.1,
                        corner_radius=10,
                        border_color= None,
                        bg_color="#f6f6f6"
                        )
    return btn

def frame_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "#37C940",
                        height= 60.7,
                        width= 147.1,
               
                        corner_radius=10,
                        border_color= "#37C940",
                        bg_color="#D1C7BB",
                        fg_color= "#282E2D"
                        )
    return btn

def register_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "#37C940",
                        height= 60.7,
                        width= 147.1,
                        corner_radius=10,
                        border_color= "#37C940",
                        bg_color="#BEBEBE",
                        fg_color= "#282E2D"
                        )
    return btn

def login_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "#37C940",
                        height= 60.7,
                        width= 147.1,
                        corner_radius=10,
                        border_color= "#37C940",
                        bg_color="#D3C9BE",
                        fg_color= "#282E2D"
                        )
    return btn

def back_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "#FDBD2F",
                        height= 60.7,
                        width= 147.1,
                        corner_radius=10,
                        border_color= "#B8621B",
                        bg_color="#F6F6F6",
                        fg_color= "#282E2D"
                        )
    return btn

def no_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "#F9544D",
                        height= 60.7,
                        width= 147.1,
                        corner_radius=10,
                        border_color= "#B8621B",
                        bg_color="#D1C7BB",
                        fg_color= "#282E2D"
                        )
    return btn

def regno_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=18)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "#F9544D",
                        height= 60.7,
                        width= 147.1,
                        corner_radius=10,
                        border_color= "#B8621B",
                        bg_color="#BEBEBE",
                        fg_color= "#282E2D"
                        )
    return btn

def exit_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=14)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="#282E2D",
                        hover= True,
                        hover_color= "#F9544D",
                        height= 20,
                        width= 20,
                        corner_radius=None,
                        border_color= None,
                        bg_color="#f6f6f6",
                        fg_color= "#f6f6f6"
                        )
    return btn

def entry_style(master, placeholder_text):
    entry_name = ctk.CTkEntry(
                        master,
                        placeholder_text = placeholder_text,
                        placeholder_text_color="Gray",
                        font=('Poppins', 17),
                        text_color="black",
                        width=382.2,
                        height=49.2,
                        border_width=1,
                        border_color= "#EEEEEE",
                        bg_color="#BDBCBB",
                        fg_color= "#EEEEEE",
                        corner_radius=10
                        )
    return entry_name

def entry_style_csc(master, placeholder_text):
    entry_name = ctk.CTkEntry(
                        master,
                        placeholder_text = placeholder_text,
                        placeholder_text_color="Gray",
                        font=('Poppins', 18),
                        text_color="black",
                        width=320.1,
                        height=49.8,
                        border_width=1,
                        border_color= "#EEEEEE",
                        bg_color="#D3C9BE",
                        fg_color= "#EEEEEE",
                        corner_radius=20
                        )
    return entry_name




def webcam_style_label(window):
    label = tk.Label(window)
    label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    return label

def webcam_style_label2(window):
    label = tk.Label(window)
    label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    return label

def webcam_style_label3(window):
    label = tk.Label(window)
    label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    return label

def webcam_style_label4(window):
    label = tk.Label(window)
    label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    return label