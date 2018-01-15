import tkinter as tk
from tkinter import messagebox
from middleend import operations as o

def login():
    def check():
        def addCourse():
            name=coursename.get()
            fees=coursefees.get()
            print(name,fees)
            o.insertIntoCourse(name, fees)
            
        user=username.get()
        pwd=password.get()
        bool,value=o.login(user,pwd)
        if(bool and value==999):
            root3=tk.Tk()
            root2.destroy()
            label1=tk.Label(root3,text="CourseName")
            label1.grid(row=1,column=1)
            label2=tk.Label(root3,text="CourseFees")
            label2.grid(row=2,column=1)
            coursename=tk.Entry(root3)
            coursename.grid(row=1,column=2)
            
            coursefees=tk.Entry(root3)
            coursefees.grid(row=2,column=2)
            button1=tk.Button(root3,text="submit",command=addCourse)
            button1.grid(row=3,column=2)
            
            root3.mainloop()    

            
            
            root3.mainloop()
        elif(bool and value==000):
            root4=tk.Tk()
            root2.destroy()
           
            
            root4.mainloop()
        elif(bool==False and value==0):
            print("Invalid Credential")
#             
            
        
        
        
    root2=tk.Tk()
    label1=tk.Label(root2,text="UserName")
    label1.grid(row=1,column=1)
    label2=tk.Label(root2,text="password")
    label2.grid(row=2,column=1)
    username=tk.Entry(root2)
    username.grid(row=1,column=2)
    
    password=tk.Entry(root2,show="*")
    password.grid(row=2,column=2)
    button1=tk.Button(root2,text="submit",command=check)
    button1.grid(row=3,column=2)
    
    root1.destroy()
    root2.mainloop()    

root1=tk.Tk()
b1=tk.Button(root1,text="Login",command=login)
b1.grid(row=1,column=1)    
b2=tk.Button(root1,text="register")
b2.grid(row=2,column=1)
root1.mainloop()
    
    
    



