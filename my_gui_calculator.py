from tkinter import *
from tkinter import messagebox


class Simple_gui_calculator:
    def __init__(self,root):
        self.f=Frame(root,height=500,width=700,bg="skyblue") #create frame
        self.f.propagate(0)
        self.f.pack()#attach the frame with root window
        self.FONT=("Comic Sans MS",20,"bold")
        
        
       
        #create label
        self.head=Label(self.f,text="Simple Gui calculator",bg="skyblue",font=self.FONT)#heading
        self.head.grid(row=0,column=0,pady=20,padx=20,columnspan=2)
        self.n1=Label(self.f,text="Enter 1st Integer : ",bg="skyblue",font=self.FONT)#first no
        self.n1.grid(row=1,column=0,padx=20,pady=20)
        self.operator=Label(self.f,text="Operators",bg="skyblue",font=self.FONT)#operator list
        self.operator.grid(row=0,column=2,columnspan=2,padx=20,pady=20)#columnspan merges 2 no of columns cells
        self.n2=Label(self.f,text="Enter 2nd Integer : ",bg="skyblue",font=self.FONT)#2nd no
        self.n2.grid(row=2,column=0,padx=20,pady=20)
        self.result=Label(self.f,text="Result : ",bg="skyblue",font=self.FONT)
        self.result.grid(row=3,column=0,padx=20,pady=20)

        #create label to display result
        self.ans=Label(self.f,bg="skyblue",font=self.FONT)
        #self.ans.grid(row=3,column=1,padx=20,pady=20)

        #create text box for input
        
        self.t1=Text(self.f,width=20,height=2,borderwidth=1)#for 1st number
        self.t1.grid(row=1,column=1,padx=20,pady=20)
        self.t1.configure(font=("Comic Sans MS",10,"bold"))
        self.t2=Text(self.f,width=20,height=2,borderwidth=1)#for 1st number
        self.t2.grid(row=2,column=1,padx=20,pady=20)
        self.t2.configure(font=("Comic Sans MS",10,"bold"))
        self.t1.focus_set()#sets focus to 1st textbox

        #create buttons:
        #addition
        self.add=Button(self.f,text="+",width=6,height=1,font=self.FONT,bg="skyblue",command=self.plus)
        self.add.grid(row=1,column=2,padx=20,pady=20)
        #subtract
        
        self.sub=Button(self.f,text="-",width=6,height=1,bg="skyblue",font=self.FONT,command=self.minus)
        self.sub.grid(row=1,column=3,padx=20,pady=20)
        #multiply
        self.mul=Button(self.f,text="*",width=6,height=1,font=self.FONT,bg="skyblue",command=self.multiply)
        self.mul.grid(row=2,column=2,padx=20,pady=20)
        #Division
        self.div=Button(self.f,text="/",width=6,height=1,font=self.FONT,bg="skyblue",command=self.divide)
        self.div.grid(row=2,column=3,padx=20,pady=20)
        #submit
        self.submit=Button(self.f,text="Submit",width=6,height=1,font=self.FONT,bg="skyblue",command=self.submit)
        self.submit.grid(row=3,column=2,padx=20,pady=20)
        #reset
        self.reset=Button(self.f,text="Reset",width=6,height=1,font=self.FONT,bg="skyblue",command=self.clear)
        self.reset.grid(row=3,column=3,padx=20,pady=20)
        
        self.check_button=""  #to check buttton whether it has been clicked or not

    def plus(self):
        if self.add["text"]=="+":
            num1=self.t1.get("1.0","end-1c")
            num2=self.t2.get("1.0","end-1c")
            sum=eval(num1)+eval(num2)
            self.check_button="+" #it has been clicked
            return sum

    def minus(self):
        if self.sub["text"]=="-":
            num1=self.t1.get("1.0","end-1c")
            num2=self.t2.get("1.0","end-1c")
            difference=eval(num1)-eval(num2)
            self.check_button="-" #it has been clicked
            return difference

    def multiply(self):
        if self.mul["text"]=="*":
            num1=self.t1.get("1.0","end-1c")
            num2=self.t2.get("1.0","end-1c")
            product=eval(num1) * eval(num2)
            self.check_button="*" #it has been clicked
            return product

    def divide(self):
        if self.div["text"]=="/":
            num1=self.t1.get("1.0","end-1c")
            num2=self.t2.get("1.0","end-1c")
            qut=eval(num1)/eval(num2)
            self.check_button="/" #it has been clicked
            return qut
    
    def submit(self):
        #to submit final input:
        n1=self.t1.get("1.0","end-1c")#1st number
        n2=self.t2.get("1.0","end-1c")#2nd number
        WARN_TEXT="enter an Integer"
        if n1=="" and n2=="":
            # both text box are empty
            self.t1.focus_set()
            messagebox.showwarning("showwarning","No input value given "+WARN_TEXT)

        elif n1=="" and n2!="":
            #n1 is empty and n2 is not a number
            if n2.isnumeric()==False:
                self.t2.delete("1.0","end")#delete
                self.t1.focus_set()
                messagebox.showwarning("showwarning",WARN_TEXT+" in both textbox")

            else:
                self.t1.focus_set()
                messagebox.showwarning("showwarning",WARN_TEXT+" in 1st textbox")
                
        elif (n2=="" and n1!=""):
            #n2 is empty and n1 is not a number
            if n1.isnumeric()==False:
                self.t1.delete("1.0","end")#delete
                self.t1.focus_set()
                messagebox.showwarning("showwarning",WARN_TEXT+"in both textbox")

            else:
                self.t2.focus_set()
                messagebox.showwarning("showwarning",WARN_TEXT+" in 2nd textbox")
                
        else:
            #if both are not empty:    
            if n1.isnumeric()==True and n2.isnumeric()==True:
                #if both the numbers are integers
                
                if self.check_button=="+":
                    self.ans["text"]=str(self.plus())
                    self.ans.grid(row=3,column=1,padx=20,pady=20)

                if self.check_button=="-":
                    self.ans["text"]=str(self.minus())
                    self.ans.grid(row=3,column=1,padx=20,pady=20)

                if self.check_button=="*":
                    self.ans["text"]=str(self.multiply())
                    self.ans.grid(row=3,column=1,padx=20,pady=20)

                if self.check_button=="/":
                    self.ans["text"]=str(self.divide())
                    self.ans.grid(row=3,column=1,padx=20,pady=20)

            elif n1.isnumeric()==True and n2.isnumeric()==False:
                self.t2.delete("1.0","end")#delete
                self.t2.focus_set()
                messagebox.showwarning("showwarning",WARN_TEXT+" in 2nd textbox")

            elif n2.isnumeric()==True and n1.isnumeric()==False:
                self.t1.delete("1.0","end")#delete
                self.t1.focus_set()
                messagebox.showwarning("showwarning",WARN_TEXT+" in 1nd textbox")

            else:
                #both are text
                self.t1.delete("1.0","end")
                self.t2.delete("1.0","end")
                self.t1.focus_set()
                messagebox.showwarning("showwarning","Wrong input given "+WARN_TEXT+" in both textbox")
    

    def clear(self):
        #deletes everyting from both textbox
        #if  self.reset["text"]=="Reset":
        self.t1.delete("1.0","end")
        self.t2.delete("1.0","end")
        self.t1.focus_set()
        self.ans["text"] = ""#clear if any result is displayed

r=Tk()#root window
r.title("Simple_gui_calculator")
my_cal=Simple_gui_calculator(r)
r.mainloop()
