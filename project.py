from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login_System:
	def _init_(self,root):
		self.root = root
		self.root.title("LOGIN SYSTEM | Rajnish Kushwaha")
		self.root.geometry("1350x700+0+0")

		self.phone_image=PhotoImage(file="E:\study\2nd semester\cse 229 java\images\phone.jpg")
		self.lbl_Phone_image=Label(self.root,image=self.phone_image).place(x=200,y=90)

		login_frame=Frame(self.root,bd=2,relief=RIDGE)
		login_frame.place(x=650,y=90,width=350,height=460)

		title=Label(login_frame,text="LOGIN SYSTEM",font=("Arial",20,"bold"),bg="blue").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
		txt_user=Entry(login_frame,textvariable=self,font=("Andalus",15),bg="#ECECEC").place(x=50,y=140)

        lbl_user=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
		txt_user=Entry(login_frame,textvariable=self,font=("Andalus",15),bg="#ECECEC").place(x=50,y=140)

		btn_login=Button(login_frame,text="Log In",font=("Arial Rounded MT Bold"),bg="#00b0f0",fg="white").place(x=50,y=300,width=250,height=35)

		hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
		or_=Label(login_frame,text="OR",bg="white",fg="black",font=("times new roman")).place(x=150,y=360)

		btn_forget=Button(login_frame,text="Forget Password",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

		register_frame=Frame(self.root,bd=2,relief=RIDGE,bf="white")
		register_frame.place(x=650,y=570,width=350,height=60)

		lbl_reg=Label(register_frame,text="Don't have an account?",font=("times new roman"),bg="white").place(x=40,y=20)
		btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13),bg="white",activebackground="white",activeforeground="#00759E").place(x=200,y=390)

		self.im1=ImageTk.PhotoImage(file="E:\study\2nd semester\cse 229 java\images/1.png")
		self.im2=ImageTk.PhotoImage(file="E:\study\2nd semester\cse 229 java\images/2.png")
		self.im3=ImageTk.PhotoImage(file="E:\study\2nd semester\cse 229 java\images/3.png")

		self.lbl_change_image=Label(self.root)
		self.lbl_change_image.place(x=240,y=50,width=370,height=662)

	def  animate(self):
		self.im=self.im1
		self.im1=self.im2
		self.im2=self.im3
		self.im3=self.im
		self.lbl_change_image.config(image=self.im)
		self.lbl_change_image.after(2000,self.animate)
				

root = Tk()
obj = Login_System(root)
root.mainloop()