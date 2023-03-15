#BMI CALCULATOTR
#first crate new frame and window:
from tkinter import *

def bmi():
    #to calculate BMI:
    class Calculate:
        def __init__(self,root):
            self.f= Frame(root,height=500,width=400,bg="LightBlue1")
            self.f.propagate(0)
            self.f.pack()

            self.head = Label(self.f,text="BMI CALCULATOR",height=2,width=20,font=("Courier",-25,"bold"),bg="LightBlue1")
            self.head.place(x=50,y=50)
            self.l1 = Label(self.f,text="Enter your height : ",bg="LightBlue1")
            
            self.l2 = Label(self.f,text="Enter your weight : ",bg="LightBlue1")

            #entry widgets:
            self.e1 = Entry(self.f,width=25)
            self.e2 = Entry(self.f,width=25)
            self.e2.bind("<Return>",self.display)

            #attach and place it on frame
            self.l1.place(x=50,y=150)
            self.l2.place(x=50,y=200)
            self.e1.place(x=180,y=150)
            self.e2.place(x=180,y=200)

            #final display label: && update in the display 
            self.lab1 = Label(self.f,text="",bg="LightBlue1")
            self.lab1.place(x=50,y=240)

        def cal(self):
            weight = self.e2.get()
            height = self.e1.get()

            try:
                weight = float(weight)
            except(ValueError):
                return 0

            try:
                height=float(height)
            except(ValueError):
                return 0

            #if all inputs are in numbers:
            res = weight/(height/100)**2
            return res

        def display(self,event):
            res = self.cal()
           
            #create final display  labels
            
            if (type(res) == float):
                
                str1 = "Your BMR : "
                bmr_res = str(round(res,3))
                if res<18.5:
                    status = str1 + bmr_res + "\nStatus : "+"Underweight"
                elif res>=18.5 and res<=24.9:
                    status = str1 + bmr_res + "\nStatus : "+"Healthy"
                elif res>=25.0 and res<=29.9:
                    status = str1 + bmr_res + "\nStatus : "+"OverWeight"
                else:
                    status = str1 + bmr_res + "\nStatus : "+"Obesity"
            else:
                #non numeric input or blank
                status = "Give a numeric input"
            
            
            self.lab1.config(text=status)#update the result

    root = Tk()
    root.iconbitmap("E:/OLD_PC_FILES/PROJECTS_PYTHON/BMI AND BMR CALCULATOR/bmi.ico")
    root.title("BMI CALCULATOR")
    x = Calculate(root) 
    root.maxsize(400,290)
    root.mainloop()
            
            

     
def bmr():
    #bmr calculator:
    class Calculate:
        def __init__(self,root):
            
            self.f = Frame(root,height=500,width=400,bg="LightBlue1")
            self.f.propagate(0)
            self.f.pack()
            self.head = Label(self.f,text="BMR CALCULATOR",height=2,width=20,font=("Courier",-30,"bold"),bg="LightBlue1")
            self.head.place(x=35,y=20)
            
            

            #create radio button
            self.gender = Label(self.f,text="GENDER :",bg="LightBlue1")

            self.age = Label(self.f,text="AGE :",bg="LightBlue1")
            self.height = Label(self.f,text="HEIGHT : ",bg="LightBlue1")
            self.weight = Label(self.f,text="WEIGHT : ",bg="LightBlue1")
            self.gender.place(x=50,y=100)
            
            self.age.place(x=50,y=150)
            self.height.place(x=50,y=200)
            self.weight.place(x=50,y=250)
            
            
            #display result :
            self.result = Label(self.f,text="",bg="LightBlue1")
            self.result.place(x=50,y=300)


            #entry box for age,height and weight:
            self.gender_opt = Entry(self.f,width=5)#gender
            self.e1 = Entry(self.f,width=10)#age
            self.e2 = Entry(self.f,width=10)#height
            self.e3 = Entry(self.f,width=10)#weight
            self.e3.bind("<Return>",self.display)

            self.e1.place(x=110,y=150)
            self.e2.place(x=110,y=200)
            self.e3.place(x=110,y=250)
            self.gender_opt.place(x=110,y=100)

        def cal(self):
          
            height = self.e2.get()
            weight = self.e3.get()
            age = self.e1.get()
            gender = self.gender_opt.get()
            


            try:
                weight = float(weight)
                height=float(height)
                age=float(age)
            except(ValueError):
                return 0

            

            
            if gender == "m":
                #male
                ans = round(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age),3)
                print(ans)
                return  ans
            elif gender == "f":
                #female
                ans = round(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age),3)
                return ans
                
        

        def display(self,event):
            #to display final result
            res = self.cal()
            if res == None:
                self.result.config(text="Enter M for male or F for female in gender text box.")
            elif(res == 0):
                self.result.config(text="Give an numeric input")
            else:
                self.result.config(text="Your BMR IS : "+str(res)+"Calories/day")
    
    root=Tk()
    root.maxsize(400,360)
    root.iconbitmap("E:/OLD_PC_FILES/PROJECTS_PYTHON/BMI AND BMR CALCULATOR/bmr_nlV_2.ico")
    root.title("BMR CALCULATOR")
    x = Calculate(root)
    root.mainloop()


##########################################################$########               MAIN FUNCTION           ################################################################
root = Tk()
root.title("BMI AND BMR CALCULATOR")
root.geometry("420x500")
root.wm_iconbitmap("E:\OLD_PC_FILES\PROJECTS_PYTHON\BMI AND BMR CALCULATOR\logo.ico")

root.maxsize(420,500)

c = Canvas(root,bg="RoyalBlue1",height=500,width=300)
c.pack()
fntt = ("Helvetica",10,"bold")
bmi_txt= c.create_text(210,170,text="* Body mass index (BMI) is a measure of body fat \nbased on height and weight that applies to adult \nmen and women.",font=fntt)
bmr_txt = c.create_text(210,300,text="      * Basal metabolic rate measures the minimum amount\n of calories that your body needs to perform necessary\n functions.",font=fntt)
c.pack(fill = "both", expand = True)

fnt=("Helvetica",18,"bold")
c.create_text( 200, 100, text = "BMI AND BMR CALCULATOR",font=fnt)
bmi_button = Button(root,text="BMI",width=15,height=1,command=lambda:bmi(),activebackground="yellow")
bmi_button.pack()
bmi_button.place(x=140,y=210)

bmr_button = Button(root,text="BMR",width=15,height=1,command=lambda:bmr(),activebackground="yellow")
bmr_button.pack()
bmr_button.place(x=140,y=330)


root.mainloop()