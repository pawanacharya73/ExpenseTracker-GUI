import customtkinter as ctk
from PIL import Image, ImageTk
# import time

def main():
    # login window
    login = ctk.CTk()
    login.title("Login | Expense Tracker")


    # defining functions
    def signup_page():
        login.withdraw()
        login.destroy()
        import signup
        signup.main()
        
        

    def toggle_password():
        if password_entry.cget("show") == "*":
            password_toggle.configure(image=eyehide)
            password_entry.configure(show="")
        else:
            password_toggle.configure(image=eyeopen)
            password_entry.configure(show="*")

    def zoom_window():
        login.state('zoomed')
        
    login.resizable(False, False)
    login.after(1, lambda: zoom_window())

    # setting the app logo to nothing cus we didn't like the way it looked
    login.iconbitmap(bitmap="assets/blank.ico")

    # fullscreen windowded mode


   

    # defining images
    logo1 = ctk.CTkImage(dark_image=Image.open(
        "assets/applogo1.png"), size=(30, 30))
    logo2 = ctk.CTkImage(dark_image=Image.open(
        "assets/applogo2.png"), size=(350, 350))
    eyeopen = ctk.CTkImage(dark_image=Image.open(
        "assets/view.png"), size=(45, 45))
    eyehide = ctk.CTkImage(dark_image=Image.open(
        "assets/hide.png"), size=(45, 45))


    # Login frame #FAEBEE
    login_frame = ctk.CTkFrame(login, fg_color="#FAEBEE",
                            width=1100, height=900, corner_radius=0)
    login_frame.pack(side="left")

    # Right frame #333D79
    right_frame = ctk.CTkFrame(login, fg_color="#333D79",
                            width=500, height=900, corner_radius=0)
    right_frame.pack(side="right")

    # Login to your account
    signin_text = ctk.CTkLabel(login, text="Login to Your Account", font=(
        'Lato', 56, "bold"), text_color="#333D79", bg_color="#FAEBEE")
    signin_text.place(x=250, y=200)

    canvas = ctk.CTkCanvas(login, width=550, height=2, bg="#746F7A")
    canvas.place(x=690, y=345, anchor="center")

    # username and password entries
    username_entry = ctk.CTkEntry(login, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Username",
                                placeholder_text_color="#746F7A", font=("Lato", 28), width=330, corner_radius=28, text_color="black", height=70)
    username_entry.place(x=543, y=390, anchor="center")

    password_entry = ctk.CTkEntry(login, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Password",
                                show="*", placeholder_text_color="#746F7A", font=("Lato", 28), width=330, corner_radius=28, text_color="black", height=70,)
    password_entry.place(x=543, y=490, anchor="center")

    # login button
    login_button = ctk.CTkButton(login, text="Login", text_color="#FAEBEE", bg_color="#FAEBEE", fg_color="#333D79",
                                corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#293161", width=150)
    login_button.place(x=543, y=600, anchor="center")

    # app logo top right
    logo_right = ctk.CTkLabel(login, image=logo2, text="", fg_color="#333D79")
    logo_right.place(x=1315, y=150, anchor="center")
    trademark = ctk.CTkLabel(login, text="™", font=(
        'Lato', 28, "bold"), text_color="#FAEBEE", bg_color="#333D79")
    trademark.place(x=1440, y=60)

    # Create an account right now
    new_here = ctk.CTkLabel(login, text="New here?", font=(
        'Lato', 64, "bold"), text_color="#FAEBEE", bg_color="#333D79")
    new_here.place(x=1315, y=350, anchor="center")
    description = ctk.CTkLabel(login, text="Create an account right now\nand get your expenses right.\nHappy tracking!!!", font=(
        'Lato', 20, "bold"), text_color="#FAEBEE", bg_color="#333D79")
    description.place(x=1315, y=463, anchor="center")

    # signup button
    signup_button = ctk.CTkButton(login, text="Sign up", text_color="#333D79", bg_color="#333D79",
                                fg_color="#FAEBEE", corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#efbec0", command=signup_page)
    signup_button.place(x=1315, y=600, anchor="center")

    # footer stuff
    footer_text = ctk.CTkLabel(login, text="Expense Tracker", font=(
        'Lato', 24, "bold"), text_color="#333D79", bg_color="#FAEBEE")
    footer_text.place(x=10, y=800)
    # show/hide password
    password_toggle = ctk.CTkButton(login, image=eyeopen, text="", fg_color="#FAEBEE",
                                    bg_color="#FAEBEE", width=16, height=16, hover_color="#FAEBEE", command=toggle_password)
    password_toggle.place(x=740, y=490, anchor="center")

    login.mainloop()

if __name__ == "__main__":
    main()
