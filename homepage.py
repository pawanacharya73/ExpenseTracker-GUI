import customtkinter as ctk
from PIL import Image, ImageTk

# root window
root = ctk.CTk()

# fullscreen windowded mode
root.after(0, lambda: root.state('zoomed'))

# Login frame #FAEBEE
login_frame = ctk.CTkFrame(root, fg_color="#FAEBEE", width=1100, height=900, corner_radius=0)
login_frame.pack(side="left")

# Right frame #333D79
right_frame = ctk.CTkFrame(root, fg_color="#333D79", width=500, height=900, corner_radius=0)
right_frame.pack(side="right")

# Login to your account
signin_text = ctk.CTkLabel(root, text="hey testtttttttttt\nthisss is hoemfkjhekjpageee", font=('Lato', 56, "bold"), text_color="#333D79", bg_color="#FAEBEE")
signin_text.place(x = 250, y= 200)

username_entry = ctk.CTkEntry(root, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Username", placeholder_text_color="#746F7A", font=("Lato", 28), width=330, corner_radius=28, text_color="black", height=70 )
username_entry.place(x= 543, y=350, anchor = "center")

password_entry = ctk.CTkEntry(root, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Password", show = "*" ,placeholder_text_color="#746F7A", font=("Lato", 28), width=330, corner_radius=28, text_color="black", height=70 )
password_entry.place(x= 543, y=450, anchor = "center")


# login button
login_button = ctk.CTkButton(root, text="Login", text_color="#FAEBEE", bg_color="#FAEBEE", fg_color="#333D79", corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#293161", )
login_button.place(x= 543, y = 600, anchor = "center")

# Create an account right now
new_here = ctk.CTkLabel(root, text="New here?", font=('Lato', 64, "bold"), text_color="#FAEBEE", bg_color="#333D79")
new_here.place(x = 1315, y= 350, anchor = "center")
description = ctk.CTkLabel(root, text="Create an account right now\nand get your expenses right.\nHappytracking!!!", font=('Lato', 22, "bold"), text_color="#FAEBEE", bg_color="#333D79")
description.place(x = 1315, y= 460, anchor = "center")

# signup button
signup_button = ctk.CTkButton(root, text="Sign up", text_color="#333D79", bg_color="#333D79", fg_color="#FAEBEE", corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#efbec0", )
signup_button.place(x= 1315, y = 600, anchor = "center")




root.mainloop()

