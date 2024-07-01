import customtkinter as ctk
from PIL import Image, ImageTk


def main():
    # signup window
    signup = ctk.CTk()
    signup.title("Sign Up | Expense Tracker")

    # fullscreen windowded mode
    def zoom_window():
        signup.state('zoomed')
    signup.resizable(False, False)
    signup.after(1, lambda: zoom_window())

    def go_back():
        signup.destroy()
        import login
        login.main()

    # setting the app logo to nothing cus we didn't like the way it looked
    signup.iconbitmap(bitmap="assets/blank.ico")

    
    # defining images
    logo1 = ctk.CTkImage(dark_image=Image.open(
        "assets/applogo1.png"), size=(30, 30))
    logo2 = ctk.CTkImage(dark_image=Image.open(
        "assets/applogo2.png"), size=(350, 350))
    demochart = ctk.CTkImage(dark_image=Image.open(
        "assets/DemoChart.png"), size=(413, 310))
    back = ctk.CTkImage(dark_image=Image.open(
        "assets/back.png"), size=(40, 40))
    forward = ctk.CTkImage(dark_image=Image.open(
        "assets/forward.png"), size=(40, 40))


    # Login frame #FAEBEE
    login_frame = ctk.CTkFrame(signup, fg_color="#FAEBEE",
                            width=1100, height=900, corner_radius=0)
    login_frame.pack(side="right")

    # left frame #333D79
    left_frame = ctk.CTkFrame(signup, fg_color="#333D79",
                            width=500, height=900, corner_radius=0)
    left_frame.pack(side="left")

    #  Create a new account
    signup_text = ctk.CTkLabel(signup, text="Create a new account", font=(
        'Lato', 56, "bold"), text_color="#333D79", bg_color="#FAEBEE")
    signup_text.place(x=975, y=130, anchor = "center")

    canvas = ctk.CTkCanvas(signup, width=550, height=2, bg="#746F7A")
    canvas.place(x=1220, y=230, anchor="center")

    # email, username, name, and gender fields
    email_entry = ctk.CTkEntry(signup, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Username",
                                placeholder_text_color="#746F7A", font=("Lato", 28), width=400, corner_radius=28, text_color="black", height=60)
    email_entry.place(x=975, y=300, anchor="center")

    firstname_entry = ctk.CTkEntry(signup, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="First name",
                                placeholder_text_color="#746F7A", font=("Lato", 28), width=190, corner_radius=28, text_color="black", height=60)
    firstname_entry.place(x=870, y=372, anchor="center")

    lastname_entry = ctk.CTkEntry(signup, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Last name",
                                placeholder_text_color="#746F7A", font=("Lato", 28), width=190, corner_radius=28, text_color="black", height=60)
    lastname_entry.place(x=1083, y=372, anchor="center")

    createpassword_entry = ctk.CTkEntry(signup, bg_color="#FAEBEE", fg_color="#C8C0D2", border_color="#C8C0D2", placeholder_text="Create password",
                                placeholder_text_color="#746F7A", font=("Lato", 28), width=400, corner_radius=28, text_color="black", height=60)
    createpassword_entry.place(x=975, y=444, anchor="center")

    # gender selection
    male = ctk.CTkRadioButton(signup, text="Male", bg_color="#FAEBEE", font=('Lato', 18, "bold"), text_color="#333D79")
    male.place(x = 975, y= 500, anchor = "center")

    # signup button
    signup_button = ctk.CTkButton(signup, text="Sign Up", text_color="#FAEBEE", bg_color="#FAEBEE", fg_color="#333D79",
                                corner_radius=30, font=('Lato', 25, "bold"), height=55, hover_color="#293161", width=150)
    signup_button.place(x=975, y=700, anchor="center")

    # app logo top left
    logo_right = ctk.CTkLabel(signup, image=logo2, text="", fg_color="#333D79")
    logo_right.place(x=216, y=150, anchor="center")
    trademark = ctk.CTkLabel(signup, text="™", font=(
        'Lato', 28, "bold"), text_color="#FAEBEE", bg_color="#333D79")
    trademark.place(x=350, y=60)

    # demo chart
    chart = ctk.CTkLabel(signup, image=demochart, text="")
    chart.place(x = 200, y = 400, anchor = "center")


    # did you know
    new_here = ctk.CTkLabel(signup, text="Did you know?", font=(
        'Lato', 30, "bold"), text_color="#FAEBEE", bg_color="#333D79")
    new_here.place(x=215, y=650, anchor="center")
    description = ctk.CTkLabel(signup, text="Tracking spending can help you\ncut unnecessary expenses and\nboost your savings by 10%!", font=(
        'Lato', 24), text_color="#FAEBEE", bg_color="#333D79")
    description.place(x=215, y=745, anchor="center")


    # back and forward buttons
    backbutton = ctk.CTkButton(signup, image=back, text="", fg_color="#FAEBEE", width=20, height=20, bg_color="#FAEBEE",command=lambda: go_back(), hover_color = "#FAEBEE")
    backbutton.place(x=470, y=30, anchor="center")
    forwardbutton = ctk.CTkButton(signup, image=forward, text="", fg_color="#FAEBEE", width=15, height=20, bg_color="#FAEBEE", command="", hover_color="#FAEBEE")
    forwardbutton.place(x=520, y=30, anchor="center")


    # footer stuff
    footer_text = ctk.CTkLabel(signup, text="Expense Tracker", font=(
        'Lato', 24, "bold"), text_color="#333D79", bg_color="#FAEBEE")
    footer_text.place(x=1330, y=800)

    signup.mainloop()


if __name__ == "__main__":
    main()