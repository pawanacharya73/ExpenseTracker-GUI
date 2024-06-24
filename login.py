import customtkinter as ctk
from PIL import Image, ImageTk

# root window
root = ctk.CTk()
root.title("Login | Expense Tracker")

#setting the app logo to nothing cus we didn't like the way it looked
root.iconbitmap(bitmap="assets/blank.ico")

# fullscreen windowded mode
root.resizable(False, False)
root.after(0, lambda: root.state('zoomed'))

# defining images
logo1 = ctk.CTkImage(dark_image= Image.open("assets/applogo1.png"), size=(30, 30))
logo2 = ctk.CTkImage(dark_image= Image.open("assets/applogo2.png"), size=(350, 350))

# Login frame #FAEBEE
login_frame = ctk.CTkFrame(root, fg_color="#FAEBEE", width=1100, height=900, corner_radius=0)
login_frame.pack(side="left")

# Right frame #333D79
right_frame = ctk.CTkFrame(root, fg_color="#333D79", width=500, height=900, corner_radius=0)
right_frame.pack(side="right")

# Login to your account
signin_text = ctk.CTkLabel(root, text="Login to Your Account", font=('Lato', 56, "bold"), text_color="#333D79", bg_color="#FAEBEE")
signin_text.place(x = 250, y= 200)

canvas = ctk.CTkCanvas(root, width=550, height=2, bg = "#746F7A")
canvas.place(x = 690, y= 360, anchor= "center")

# username and password entries
username_entry = ctk.CTkEntry(root, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Username", placeholder_text_color="#746F7A", font=("Lato", 28), width=330, corner_radius=28, text_color="black", height=70 )
username_entry.place(x= 543, y=390, anchor = "center")

password_entry = ctk.CTkEntry(root, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Password", show = "*" ,placeholder_text_color="#746F7A", font=("Lato", 28), width=330, corner_radius=28, text_color="black", height=70 )
password_entry.place(x= 543, y=490, anchor = "center")

# login button
login_button = ctk.CTkButton(root, text="Login", text_color="#FAEBEE", bg_color="#FAEBEE", fg_color="#333D79", corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#293161", width=150)
login_button.place(x= 543, y = 600, anchor = "center")

# app logo top right
logo_right = ctk.CTkLabel(root, image=logo2, text="", fg_color="#333D79")
logo_right.place(x = 1315, y = 150, anchor = "center")
trademark = ctk.CTkLabel(root, text="™", font=('Lato', 28, "bold"), text_color="#FAEBEE", bg_color="#333D79")
trademark.place(x = 1440, y = 60)

# Create an account right now
new_here = ctk.CTkLabel(root, text="New here?", font=('Lato', 64, "bold"), text_color="#FAEBEE", bg_color="#333D79")
new_here.place(x = 1315, y= 350, anchor = "center")
description = ctk.CTkLabel(root, text="Create an account right now\nand get your expenses right.\nHappy tracking!!!", font=('Lato', 20, "bold"), text_color="#FAEBEE", bg_color="#333D79")
description.place(x = 1315, y= 463, anchor = "center")

# signup button
signup_button = ctk.CTkButton(root, text="Sign up", text_color="#333D79", bg_color="#333D79", fg_color="#FAEBEE", corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#efbec0")
signup_button.place(x= 1315, y = 600, anchor = "center")

# footer stuff
footer_text = ctk.CTkLabel(root, text="Expense Tracker", font=('Lato', 24, "bold"), text_color="#333D79", bg_color="#FAEBEE")
footer_text.place(x = 10, y = 800)

root.mainloop()
