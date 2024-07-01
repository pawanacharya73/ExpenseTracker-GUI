# from tkinter import * 

# from customtkinter import *
# from PIL import Image,ImageTk


# class App(Tk):
#     def _init_(self):
#         super()._init_()
#         self.title("Multi-Page Application")
#         self.geometry("600x600")
#         self.minsize(width=600,height=600)
#         # Container for all frames
#         self.container = Frame(self)
#         self.container.pack(fill='both', expand=True)

#         self.frames = {}
#         for F in (HomePage, ProductPage, CartPage, AccountPage):
#             page_name = F._name_
#             frame = F(parent=self.container, controller=self)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame("HomePage")

#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()
#         frame.update_title()

# class HomePage(Frame):
#     def _init_(self, parent, controller):
#         super()._init_(parent)
#         self.controller = controller
        
#         screen_height = self.winfo_screenheight()
#         screen_width = self.winfo_screenwidth()

#         image_path = "f:/college/1 semester/led projects/static/images/login1.png"  # Replace with the path to your image
#         img = Image.open(image_path)
#         img = img.resize((400, 350))  # Resize image to fit the frame if needed

#         img = ImageTk.PhotoImage(img)

#         userimage_path = "f:/college/1 semester/led projects/static/images/user.png"
#         userimg = Image.open(userimage_path)
#         userimg = userimg.resize((20, 20)) 
#         userimg = ImageTk.PhotoImage(userimg)

#         passimage_path = "f:/college/1 semester/led projects/static/images/password.png"
#         passimg = Image.open(passimage_path)
#         passimg = passimg.resize((23, 23)) 
#         passimg = ImageTk.PhotoImage(passimg)

#         emailimage_path = "f:/college/1 semester/led projects/static/images/email.png"
#         emailimg = Image.open(emailimage_path)
#         emailimg = emailimg.resize((20, 24)) 
#         emailimg = ImageTk.PhotoImage(emailimg)

#         logoimage_path = "f:/college/1 semester/led projects/static/images/bus1.png"
#         logoimg = Image.open(logoimage_path)
#         logoimg = logoimg.resize((250, 250)) 
#         logoimg = ImageTk.PhotoImage(logoimg)



#         leftoptionframe = CTkLabel(self,width=130,text="",fg_color="#333333",height=screen_height,corner_radius=0)
#         leftoptionframe.pack(side=LEFT)
#         leftoptionframe.pack_propagate(False)


#         logo = CTkLabel(leftoptionframe,image=logoimg,fg_color="#333333",text="")
#         logo.place(relx=0.5,rely=0.08,anchor=CENTER)
            
#         homebutton = CTkButton(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10,command=lambda: controller.show_frame("HomePage"))
#         homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         def on_home_enter(event):
#             homebutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             homebutton.place(x=43,rely=0.3001,anchor=CENTER)
#         homebutton.bind("<Enter>", on_home_enter)

#         def on_home_leave(event):
#             homebutton.configure(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10)
#             homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         homebutton.bind("<Leave>", on_home_leave)

#         productsbutton = CTkButton(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("ProductPage"))
#         productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         def on_products_enter(event):
#             productsbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             productsbutton.place(x=55,rely=0.3901,anchor=CENTER)
#         productsbutton.bind("<Enter>", on_products_enter)

#         def on_products_leave(event):
#             productsbutton.configure(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_width=0)
#             productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         productsbutton.bind("<Leave>", on_products_leave)
#         cartbutton = CTkButton(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("CartPage"))
#         cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         def on_cart_enter(event):
#             cartbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             cartbutton.place(x=36,rely=0.4901,anchor=CENTER)
#         cartbutton.bind("<Enter>", on_cart_enter)

#         def on_cart_leave(event):
#             cartbutton.configure(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_width=0)
#             cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         cartbutton.bind("<Leave>", on_cart_leave)
#         accountbutton = CTkButton(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         def on_account_enter(event):
#             accountbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             accountbutton.place(x=56,rely=0.5901,anchor=CENTER)
#         accountbutton.bind("<Enter>", on_account_enter)

#         def on_account_leave(event):
#             accountbutton.configure(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_width=0)
#             accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         accountbutton.bind("<Leave>", on_account_leave)
#         accountsettingbutton = CTkButton(leftoptionframe,text=" Account Settings",font=('verdana',12),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountsettingbutton.place(x=75,rely=0.8,anchor=CENTER)
#         accountsettinglabel = CTkLabel(accountsettingbutton,text="",image=passimg)
#         accountsettinglabel.place(x=0,y=0)







#         mainframe = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slategray",corner_radius=0,border_width=2,border_color="black")
#         mainframe.pack(side=LEFT)
#         mainframe.pack_propagate

#     def update_title(self):
#         self.controller.title("Home - App")

# class ProductPage(Frame):
#     def _init_(self, parent, controller):
#         super()._init_(parent)
#         self.controller = controller
#         # label = ttk.Label(self, text="Product Page")
#         # label.pack(side="top", fill="x", pady=10)

#         # button = ttk.Button(self, text="Go to Home Page",
#         #                     command=lambda: controller.show_frame("HomePage"))
#         # button.pack()
#         screen_height = self.winfo_screenheight()
#         screen_width = self.winfo_screenwidth()

#         image_path = "f:/college/1 semester/led projects/static/images/login1.png"  # Replace with the path to your image
#         img = Image.open(image_path)
#         img = img.resize((400, 350))  # Resize image to fit the frame if needed

#         img = ImageTk.PhotoImage(img)

#         userimage_path = "f:/college/1 semester/led projects/static/images/user.png"
#         userimg = Image.open(userimage_path)
#         userimg = userimg.resize((20, 20)) 
#         userimg = ImageTk.PhotoImage(userimg)

#         passimage_path = "f:/college/1 semester/led projects/static/images/password.png"
#         passimg = Image.open(passimage_path)
#         passimg = passimg.resize((23, 23)) 
#         passimg = ImageTk.PhotoImage(passimg)

#         emailimage_path = "f:/college/1 semester/led projects/static/images/email.png"
#         emailimg = Image.open(emailimage_path)
#         emailimg = emailimg.resize((20, 24)) 
#         emailimg = ImageTk.PhotoImage(emailimg)

#         logoimage_path = "f:/college/1 semester/led projects/static/images/bus1.png"
#         logoimg = Image.open(logoimage_path)
#         logoimg = logoimg.resize((250, 250)) 
#         logoimg = ImageTk.PhotoImage(logoimg)



#         leftoptionframe = CTkLabel(self,width=130,text="",fg_color="#333333",height=screen_height,corner_radius=0)
#         leftoptionframe.pack(side=LEFT)
#         leftoptionframe.pack_propagate(False)


#         logo = CTkLabel(leftoptionframe,image=logoimg,fg_color="#333333",text="")
#         logo.place(relx=0.5,rely=0.08,anchor=CENTER)
            
#         homebutton = CTkButton(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,command=lambda: controller.show_frame("HomePage"))
#         homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         def on_home_enter(event):
#             homebutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             homebutton.place(x=43,rely=0.3001,anchor=CENTER)
#         homebutton.bind("<Enter>", on_home_enter)

#         def on_home_leave(event):
#             homebutton.configure(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0)
#             homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         homebutton.bind("<Leave>", on_home_leave)

#         productsbutton = CTkButton(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10,command=lambda: controller.show_frame("ProductPage"))
#         productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         def on_products_enter(event):
#             productsbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             productsbutton.place(x=55,rely=0.3901,anchor=CENTER)
#         productsbutton.bind("<Enter>", on_products_enter)

#         def on_products_leave(event):
#             productsbutton.configure(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10)
#             productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         productsbutton.bind("<Leave>", on_products_leave)
#         cartbutton = CTkButton(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("CartPage"))
#         cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         def on_cart_enter(event):
#             cartbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             cartbutton.place(x=36,rely=0.4901,anchor=CENTER)
#         cartbutton.bind("<Enter>", on_cart_enter)

#         def on_cart_leave(event):
#             cartbutton.configure(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_width=0)
#             cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         cartbutton.bind("<Leave>", on_cart_leave)
#         accountbutton = CTkButton(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         def on_account_enter(event):
#             accountbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             accountbutton.place(x=56,rely=0.5901,anchor=CENTER)
#         accountbutton.bind("<Enter>", on_account_enter)

#         def on_account_leave(event):
#             accountbutton.configure(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_width=0)
#             accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         accountbutton.bind("<Leave>", on_account_leave)
#         accountsettingbutton = CTkButton(leftoptionframe,text=" Account Settings",font=('verdana',12),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountsettingbutton.place(x=75,rely=0.97,anchor=CENTER)
#         accountsettinglabel = CTkLabel(accountsettingbutton,text="",image=passimg)
#         accountsettinglabel.place(x=0,y=0)


#         mainframe = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slategray",corner_radius=0,border_width=2,border_color="black")
#         mainframe.pack(side=LEFT)
#         mainframe.pack_propagate

#     def update_title(self):
#         self.controller.title("Products - App")

# class CartPage(Frame):
#     def _init_(self, parent, controller):
#         super()._init_(parent)
#         self.controller = controller
#         # label = ttk.Label(self, text="Cart Page")
#         # label.pack(side="top", fill="x", pady=10)

#         # button = ttk.Button(self, text="Go to Home Page",
#         #                     command=lambda: controller.show_frame("HomePage"))
#         # button.pack()
#         screen_height = self.winfo_screenheight()
#         screen_width = self.winfo_screenwidth()

#         image_path = "f:/college/1 semester/led projects/static/images/login1.png"  # Replace with the path to your image
#         img = Image.open(image_path)
#         img = img.resize((400, 350))  # Resize image to fit the frame if needed

#         img = ImageTk.PhotoImage(img)

#         userimage_path = "f:/college/1 semester/led projects/static/images/user.png"
#         userimg = Image.open(userimage_path)
#         userimg = userimg.resize((20, 20)) 
#         userimg = ImageTk.PhotoImage(userimg)

#         passimage_path = "f:/college/1 semester/led projects/static/images/password.png"
#         passimg = Image.open(passimage_path)
#         passimg = passimg.resize((23, 23)) 
#         passimg = ImageTk.PhotoImage(passimg)

#         emailimage_path = "f:/college/1 semester/led projects/static/images/email.png"
#         emailimg = Image.open(emailimage_path)
#         emailimg = emailimg.resize((20, 24)) 
#         emailimg = ImageTk.PhotoImage(emailimg)

#         logoimage_path = "f:/college/1 semester/led projects/static/images/bus1.png"
#         logoimg = Image.open(logoimage_path)
#         logoimg = logoimg.resize((250, 250)) 
#         logoimg = ImageTk.PhotoImage(logoimg)



#         leftoptionframe = CTkLabel(self,width=130,text="",fg_color="#333333",height=screen_height,corner_radius=0)
#         leftoptionframe.pack(side=LEFT)
#         leftoptionframe.pack_propagate(False)


#         logo = CTkLabel(leftoptionframe,image=logoimg,fg_color="#333333",text="")
#         logo.place(relx=0.5,rely=0.08,anchor=CENTER)
            
#         homebutton = CTkButton(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,command=lambda: controller.show_frame("HomePage"))
#         homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         def on_home_enter(event):
#             homebutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             homebutton.place(x=43,rely=0.3001,anchor=CENTER)
#         homebutton.bind("<Enter>", on_home_enter)

#         def on_home_leave(event):
#             homebutton.configure(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0)
#             homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         homebutton.bind("<Leave>", on_home_leave)

#         productsbutton = CTkButton(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,corner_radius=10,command=lambda: controller.show_frame("ProductPage"))
#         productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         def on_products_enter(event):
#             productsbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             productsbutton.place(x=55,rely=0.3901,anchor=CENTER)
#         productsbutton.bind("<Enter>", on_products_enter)

#         def on_products_leave(event):
#             productsbutton.configure(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,corner_radius=10)
#             productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         productsbutton.bind("<Leave>", on_products_leave)
#         cartbutton = CTkButton(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10,command=lambda: controller.show_frame("CartPage"))
#         cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         def on_cart_enter(event):
#             cartbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             cartbutton.place(x=36,rely=0.4901,anchor=CENTER)
#         cartbutton.bind("<Enter>", on_cart_enter)

#         def on_cart_leave(event):
#             cartbutton.configure(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10)
#             cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         cartbutton.bind("<Leave>", on_cart_leave)
#         accountbutton = CTkButton(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         def on_account_enter(event):
#             accountbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             accountbutton.place(x=56,rely=0.5901,anchor=CENTER)
#         accountbutton.bind("<Enter>", on_account_enter)

#         def on_account_leave(event):
#             accountbutton.configure(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_width=0)
#             accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         accountbutton.bind("<Leave>", on_account_leave)
#         accountsettingbutton = CTkButton(leftoptionframe,text=" Account Settings",font=('verdana',12),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountsettingbutton.place(x=75,rely=0.97,anchor=CENTER)
#         accountsettinglabel = CTkLabel(accountsettingbutton,text="",image=passimg)
#         accountsettinglabel.place(x=0,y=0)


#         mainframe = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slategray",corner_radius=0,border_width=2,border_color="black")
#         mainframe.pack(side=LEFT)
#         mainframe.pack_propagate


#     def update_title(self):
#         self.controller.title("Cart - App")

# class AccountPage(Frame):
#     def _init_(self, parent, controller):
#         super()._init_(parent)
#         self.controller = controller
#         # frame = ttk.Frame(self,)
#         # frame.pack(fill="both")
#         # label = ttk.Label(self, text="Account Page")
#         # label.pack(side="top", fill="x", pady=10)

#         # button = ttk.Button(self, text="Go to Home Page",
#         #                     command=lambda: controller.show_frame("HomePage"))
#         # button.pack()
#         screen_height = self.winfo_screenheight()
#         screen_width = self.winfo_screenwidth()

#         image_path = "f:/college/1 semester/led projects/static/images/login1.png"  # Replace with the path to your image
#         img = Image.open(image_path)
#         img = img.resize((400, 350))  # Resize image to fit the frame if needed

#         img = ImageTk.PhotoImage(img)

#         userimage_path = "f:/college/1 semester/led projects/static/images/user.png"
#         userimg = Image.open(userimage_path)
#         userimg = userimg.resize((20, 20)) 
#         userimg = ImageTk.PhotoImage(userimg)

#         passimage_path = "f:/college/1 semester/led projects/static/images/password.png"
#         passimg = Image.open(passimage_path)
#         passimg = passimg.resize((23, 23)) 
#         passimg = ImageTk.PhotoImage(passimg)

#         emailimage_path = "f:/college/1 semester/led projects/static/images/email.png"
#         emailimg = Image.open(emailimage_path)
#         emailimg = emailimg.resize((20, 24)) 
#         emailimg = ImageTk.PhotoImage(emailimg)

#         logoimage_path = "f:/college/1 semester/led projects/static/images/bus1.png"
#         logoimg = Image.open(logoimage_path)
#         logoimg = logoimg.resize((250, 250)) 
#         logoimg = ImageTk.PhotoImage(logoimg)



#         leftoptionframe = CTkLabel(self,width=130,text="",fg_color="#333333",height=screen_height,corner_radius=0)
#         leftoptionframe.pack(side=LEFT)
#         leftoptionframe.pack_propagate(False)


#         logo = CTkLabel(leftoptionframe,image=logoimg,fg_color="#333333",text="")
#         logo.place(relx=0.5,rely=0.08,anchor=CENTER)
            
#         homebutton = CTkButton(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,command=lambda: controller.show_frame("HomePage"))
#         homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         def on_home_enter(event):
#             homebutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             homebutton.place(x=43,rely=0.3001,anchor=CENTER)
#         homebutton.bind("<Enter>", on_home_enter)

#         def on_home_leave(event):
#             homebutton.configure(leftoptionframe,text="Home",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0)
#             homebutton.place(x=41,rely=0.3,anchor=CENTER)
#         homebutton.bind("<Leave>", on_home_leave)

#         productsbutton = CTkButton(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,corner_radius=10,command=lambda: controller.show_frame("ProductPage"))
#         productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         def on_products_enter(event):
#             productsbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             productsbutton.place(x=55,rely=0.3901,anchor=CENTER)
#         productsbutton.bind("<Enter>", on_products_enter)

#         def on_products_leave(event):
#             productsbutton.configure(leftoptionframe,text="Products",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,corner_radius=10)
#             productsbutton.place(x=54,rely=0.39,anchor=CENTER)
#         productsbutton.bind("<Leave>", on_products_leave)
#         cartbutton = CTkButton(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,corner_radius=10,command=lambda: controller.show_frame("CartPage"))
#         cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         def on_cart_enter(event):
#             cartbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             cartbutton.place(x=36,rely=0.4901,anchor=CENTER)
#         cartbutton.bind("<Enter>", on_cart_enter)

#         def on_cart_leave(event):
#             cartbutton.configure(leftoptionframe,text="Cart",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=0,corner_radius=10)
#             cartbutton.place(x=35,rely=0.49,anchor=CENTER)
#         cartbutton.bind("<Leave>", on_cart_leave)
#         accountbutton = CTkButton(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10,command=lambda: controller.show_frame("AccountPage"))
#         accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         def on_account_enter(event):
#             accountbutton.configure(border_color="aquamarine",border_width=1,corner_radius=10)
#             accountbutton.place(x=56,rely=0.5901,anchor=CENTER)
#         accountbutton.bind("<Enter>", on_account_enter)

#         def on_account_leave(event):
#             accountbutton.configure(leftoptionframe,text="Account",font=('verdana',18),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",border_color="aquamarine",border_width=1,corner_radius=10)
#             accountbutton.place(x=55,rely=0.59,anchor=CENTER)
#         accountbutton.bind("<Leave>", on_account_leave)
#         accountsettingbutton = CTkButton(leftoptionframe,text=" Account Settings",font=('verdana',12),text_color="aquamarine",fg_color="#333333",hover_color="#333333",cursor="hand2",command=lambda: controller.show_frame("AccountPage"))
#         accountsettingbutton.place(x=75,rely=0.97,anchor=CENTER)
#         accountsettinglabel = CTkLabel(accountsettingbutton,text="",image=passimg)
#         accountsettinglabel.place(x=0,y=0)


#         mainframe = CTkFrame(self,width=screen_width,height=screen_height,fg_color="slategray",corner_radius=0,border_width=2,border_color="black")
#         mainframe.pack(side=LEFT)
#         mainframe.pack_propagate

        

#     def update_title(self):
#         self.controller.title("Account Info - App")


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()