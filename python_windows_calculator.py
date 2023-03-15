#to create similar calculator like inbuild calculator

from tkinter import *
from math import sqrt


class Calulator:
    def __init__(self,root):
        
        #lable and frame for final output
        self.f1=Frame(root,width=500,height=100,bg="red")
        self.f1.place(x=20,y=30,width=460,height=70)
        
        self.u_display=Label(self.f1,font=("Comic Sans MS",10,"bold"),anchor=E)
        self.u_display.place(x=0,y=0,width=460,height=25)
        
        self.l_display=Label(self.f1,font=("Comic Sans MS",20,"bold"),anchor=E,text="0")
        self.l_display.place(x=0,y=25,width=460,height=45)
        
        #frame for buttons

        self.f2=Frame(root,width=500,height=400,bg="blue")
        self.f2.place(x=20,y=110,width=460,height=393)#393
        
        #To store expression in array and there should be atleast 3 elemnets and maximum odd no of elements:
        #if there are even no of elements we will element last element.
        self.c_opt = ""
        self.c_num = ""
        self.temp = 0
        self.p_num = ""
        self.current_button = ""
        self.list = []
        self.cal_list = []
        self.d_var = "" #display variable
        self.mrs_var = 0
        
        #first row buttons:
        self.mc=self.labelframe_button(name="MC",r=0,c=0,order = self.memory_clear)
        
        self.only_labelframe(r=0,c=1)#empty label width
        self.mr=self.labelframe_button(name="MR",r=0,c=2,x=10,order = self.memory_read)
        
        self.only_labelframe(r=0,c=3)#empty label
        self.ms=self.labelframe_button(name="MS",r=0,c=4)
        
        self.only_labelframe(r=0,c=5)#empty label
        self.m_plus=self.labelframe_button(name="M+",r=0,c=6,x=10,order = self.memory_plus)
        
        self.only_labelframe(r=0,c=7)#empty label
        self.m_minus=self.labelframe_button(name="M-",r=0,c=8, order = self.memory_minus)
        
        #AFter 1st row after blank row
        self.rowonly_labelframe(r=1,c=0)#empty label height
        self.rowonly_labelframe(r=1,c=2)#empty label height
        self.rowonly_labelframe(r=1,c=4)#empty label height
        self.rowonly_labelframe(r=1,c=6)#empty label height
        self.rowonly_labelframe(r=1,c=8)#empty label height

        #2nd row button : 
        self.backspace=self.labelframe_button(name="",f=("Wingdings 3",40),r=2,c=0,y=10,order=self.back_space)
        self.only_labelframe(r=2,c=1)#empty label
        self.ce=self.labelframe_button(name="CE",r=2,c=2,x=10)
        self.only_labelframe(r=2,c=3)#empty label
        self.c=self.labelframe_button(name="C",r=2,c=4,order=self.clear_all)
        self.only_labelframe(r=2,c=5)#empty label
        self.plus_minus=self.labelframe_button(name="±",f=("Calibri",30),r=2,c=6)
        self.only_labelframe(r=2,c=7)#empty label
        self.root=self.labelframe_button(name="√",f=("Agency FB",30),r=2,c=8,order=self.sqrt)

        #after 2nd row blank row
        self.rowonly_labelframe(r=3,c=0)#empty label height
        self.rowonly_labelframe(r=3,c=2)#empty label height
        self.rowonly_labelframe(r=3,c=4)#empty label height
        self.rowonly_labelframe(r=3,c=6)#empty label height
        self.rowonly_labelframe(r=3,c=8)#empty label height

        #3rd row button :
        self.num7=self.labelframe_button(name="7",r=4,c=0,order=self.n7)
        self.only_labelframe(r=4,c=1)#empty label
        self.num8=self.labelframe_button(name="8",r=4,c=2,order=self.n8)
        self.only_labelframe(r=4,c=3)#empty label
        self.num9=self.labelframe_button(name="9",r=4,c=4,order=self.n9)
        self.only_labelframe(r=4,c=5)#empty label
        self.division=self.labelframe_button(name="/",r=4,c=6,order=self.op_div)
        self.only_labelframe(r=4,c=7)#empty label
        self.percetage=self.labelframe_button(name="%",r=4,c=8,order=self.per)

        #After 3rd row blank row :
        self.rowonly_labelframe(r=5,c=0)#empty label height
        self.rowonly_labelframe(r=5,c=2)#empty label height
        self.rowonly_labelframe(r=5,c=4)#empty label height
        self.rowonly_labelframe(r=5,c=6)#empty label height
        self.rowonly_labelframe(r=5,c=8)#empty label height

        #4th row button :
        #ask y we need to ony pass padx or pady value once
        self.num4=self.labelframe_button(name="4",r=6,c=0,y=10,order=self.n4)
        self.only_labelframe(r=6,c=1)#empty label
        self.num5=self.labelframe_button(name="5",r=6,c=2,order=self.n5)
        self.only_labelframe(r=6,c=3)#empty label
        self.num6=self.labelframe_button(name="6",r=6,c=4,order=self.n6)
        self.only_labelframe(r=6,c=5)#empty label
        self.multiply=self.labelframe_button(name="*",r=6,c=6,order=self.op_mul)
        self.only_labelframe(r=6,c=7)#empty label
        self.reciprocal=self.labelframe_button(name="1/x",r=6,c=8,order = self.reci)

        #After 4th row blank row :
        self.rowonly_labelframe(r=7,c=0)#empty label height
        self.rowonly_labelframe(r=7,c=2)#empty label height
        self.rowonly_labelframe(r=7,c=4)#empty label height
        self.rowonly_labelframe(r=7,c=6)#empty label height
        self.rowonly_labelframe(r=7,c=8)#empty label height

        #5th row button :
        self.num1=self.labelframe_button(name="1",r=8,c=0,order=self.n1)
        self.only_labelframe(r=8,c=1)#empty label
        self.num2=self.labelframe_button(name="2",r=8,c=2,order=self.n2)
        self.only_labelframe(r=8,c=3)#empty label
        self.num3=self.labelframe_button(name="3",r=8,c=4,order=self.n3)
        self.only_labelframe(r=8,c=5)#empty label
        self.subtract=self.labelframe_button(name="-",r=8,c=6,order=self.op_sub)
        self.only_labelframe(r=8,c=7)#empty label
        self.equal=self.labelframe_button(name="=",r=8,c=8,r_span=3,h=130,f=("Calibri",25),order=self.answer)

        #After 5th row blank row :
        self.rowonly_labelframe(r=9,c=0)#empty label height
        self.rowonly_labelframe(r=9,c=4)#empty label height
        self.rowonly_labelframe(r=9,c=6)#empty label height

        #6th row button :
        self.zero=self.labelframe_button(name="0",r=10,c=0,c_span=3,w=177,y=10,h=54,order=self.n0)
        self.only_labelframe(r=10,c=3)#empty label
        self.point=self.labelframe_button(name=".",r=10,c=4,h=54)
        self.only_labelframe(r=10,c=5)#empty label
        self.addition=self.labelframe_button(name="+",r=10,c=6,h=54,order=self.op_add)
        self.only_labelframe(r=10,c=7)#empty label

    def labelframe_button(self,r,c,name,x=0,y=0,h=57,w=84,f=("Calibri",20),r_span=None,c_span=None,stick="nesw",order="default"):
        """to create label frame and button"""
        #create label frame container
        label=LabelFrame(self.f2,height=h,width=w)
        label.grid(row=r,column=c,padx=0,pady=y,rowspan=r_span,columnspan=c_span)
        label.grid_rowconfigure(0,weight=1)
        label.grid_columnconfigure(0,weight=1)
        label.grid_propagate(False)
        #create button
        b=Button(label,height=2,width=10,text=name,font=f,command=order)
        b.grid(row=0,column=0,sticky=stick)

    def only_labelframe(self,r=0,c=0):
        # for column space (design)
        label=LabelFrame(self.f2,height=57,width=10,bg="blue",borderwidth=0)
        label.grid(row=r,column=c)
        label.grid_rowconfigure(0,weight=1)
        label.grid_columnconfigure(0,weight=1)
        label.grid_propagate(False)

    def rowonly_labelframe(self,r=0,c=0,h=1):
        # for row space (design)
        label=LabelFrame(self.f2,height=h,width=50,bg="blue",borderwidth=0)
        label.grid(row=r,column=c)
        label.grid_rowconfigure(0,weight=1)
        label.grid_columnconfigure(0,weight=1)
        label.grid_propagate(False)


    def n1(self):
        self.c_num += "1"
        self.current_button = "1"
        self.perform()

    def n2(self):
        self.c_num += "2"
        self.current_button = "2"
        self.perform()

    def n3(self):
        self.c_num += "3"
        self.current_button = "3"
        self.perform()

    def n4(self):
        self.c_num += "4"
        self.current_button = "4"
        self.perform()

    def n5(self):
        self.c_num += "5"
        self.current_button = "5"
        self.perform()

    def n6(self):
        self.c_num += "6"
        self.current_button = "6"
        self.perform()

    def n7(self):
        self.c_num += "7"
        self.current_button = "7"
        self.perform()

    def n8(self):
        self.c_num += "8"
        self.current_button = "8"
        self.perform()

    def n9(self):
        self.c_num += "9"
        self.current_button = "9"
        self.perform()

    def n0(self):
        self.c_num += "0"
        self.current_button = "0"
        self.perform()
        



    def clear_all(self):
        #delete all the labels
        self.l_display["text"]=""
        self.u_display["text"]=""

        #clear all elemnents
        self.c_opt = ""
        self.c_num = ""
        self.temp = 0
        self.p_num = ""
        self.current_button = ""
        self.list = []
        self.cal_list = []
        self.l_display["text"] = "0"
    
    def back_space(self):
        #to delete current num:
        if self.current_button in ("1","2","3","4","5","6","7","8","0","9"):
            new_num = self.c_num[0:len(self.c_num)-1]
            self.c_num = new_num
        
        
        self.perform()

    def sqrt(self):
        #to remove sqrt of a number
        
        if self.temp !=0 and self.cal_list[-1] in ["+","-","/","*"] and self.current_button in ("1","2","3","4","5","6","7","8","0","9"):
            #eg : 5 + sqrt(5) +sqrt(5) + ...........
            
            cal = sqrt(eval(self.c_num))
            self.c_num = "sqrt({})".format(self.c_num)
            self.l_display["text"] = cal
            
            
        elif self.temp != 0:
            #self.temp is an integer
            temp = self.temp
            self.c_num = "sqrt({})".format(str(temp))
            self.temp += sqrt(temp)
            display_lower = str(sqrt(eval(self.c_num)))
            self.l_display["text"] = display_lower
            self.temp = "sqrt(%s)"%temp
            self.u_display["text"] += "sqrt(%s)"%temp
            
            
        elif self.current_button in ("1","2","3","4","5","6","7","8","0","9"):
            temp = self.c_num
            self.c_num = str(sqrt(eval(temp)))
            self.temp =eval(self.c_num)
            self.l_display["text"] = self.c_num
            self.c_num = "sqrt(%s)"%temp
            self.u_display["text"] += "sqrt(%s)"%temp
            if "reciprocal" in self.u_display["text"]:
                self.u_display["text"] = "sqrt(reciprocal(%s))"%temp
            

        elif self.current_button in ("+","-","*","/"):
            #eg : 5 + sqrt(5)
            cal = sqrt(eval(self.p_num)) # sqrt of previous number
            self.c_num = "sqrt({})".format(self.p_num)
            self.l_display["text"] = cal
            self.u_display["text"] += "%s"%self.p_num
            
            
            
    def per(self):
        #to calculate percentage
        temp = self.c_num
        self.c_num = str(eval(temp) / 100)
        self.l_display["text"] = self.c_num
        self.c_num = "{}%".format(temp)
        self.u_display["text"] += "{}%".format(temp)

    def reci(self):
        #to remove reciprocal
        if self.c_num == "":
            self.temp = 1/self.temp
            self.l_display["text"] = str(self.temp)
            self.c_num = str(self.temp)
            
        else:
            num = self.c_num
            self.c_num = str(eval("1"+"/"+self.c_num))
            self.l_display["text"] = self.c_num
            if "sqrt" in self.u_display["text"] :
                self.u_display["text"] = "reciprocal(%s)"%num
            else:
                self.u_display["text"] += "reciprocal(%s)"%num
            
    def memory_clear(self):
        self.mrs_var = 0
    
    def memory_plus(self):
        self.u_display["text"] = ""
        self.mrs_var += eval(self.c_num)

    def memory_minus(self):
        self.u_display["text"] = ""
        self.mrs_var += eval(self.c_num) * (-1)
    
    def memory_read(self):
        self.u_display["text"] = self.mrs_var

    def op_add(self):
        
        self.c_opt = "+"
        self.p_num = self.c_num 
        self.c_num="" # clearing data
        self.current_button = "+"
            
        self.list.append(self.p_num)
        self.list.append(self.c_opt)
        self.cal_list.append(self.p_num)
        self.cal_list.append(self.c_opt)
        if self.p_num == "":
            #to remove extra blank element and previous operator
            self.list.pop(-3)
            self.list.pop(-2)
            self.cal_list.pop(-3)
            self.cal_list.pop(-2)
        self.perform()

    def op_sub(self):
        self.c_opt = "-"
        self.p_num = self.c_num 
        self.c_num="" # clearing data
        self.current_button = "-"
            
        self.list.append(self.p_num)
        self.list.append(self.c_opt)
        self.cal_list.append(self.p_num)
        self.cal_list.append(self.c_opt)
        if self.p_num == "":
            #to remove extra blank element and previous operator
            self.list.pop(-3)
            self.list.pop(-2)
            self.cal_list.pop(-3)
            self.cal_list.pop(-2)
        self.perform()

    def op_mul(self):
        self.c_opt = "*"
        self.p_num = self.c_num 
        self.c_num="" # clearing data
        self.current_button = "*"

        self.list.append(self.p_num)
        self.list.append(self.c_opt)
        self.cal_list.append(self.p_num)
        self.cal_list.append(self.c_opt)
        if self.p_num == "":
            #to remove extra blank element and previous operator
            self.list.pop(-3)
            self.list.pop(-2)
            self.cal_list.pop(-3)
            self.cal_list.pop(-2)
        self.perform()

    def op_div(self):
        self.c_opt = "/"
        self.p_num = self.c_num
        self.c_num="" # clearing data
        self.current_button = "/"

        self.list.append(self.p_num)
        self.list.append(self.c_opt)
        self.cal_list.append(self.p_num)
        self.cal_list.append(self.c_opt)
        if self.p_num == "":
            #to remove extra blank element and previous operator
            self.list.pop(-3)
            self.list.pop(-2)
            self.cal_list.pop(-3)
            self.cal_list.pop(-2)
        self.perform()

    def answer(self):
        "equal symbol"
        pass
      
    
    def perform(self):
        # main function is performed here related to operators
        print(self.list)
        print(self.cal_list)
        
        if self.current_button in ("1","2","3","4","5","6","7","8","0","9"):
            self.l_display["text"] = self.c_num
            if self.c_num == "":
                self.l_display["text"] = "0"

        if self.current_button in ("+","-","*","/"):
            self.u_display["text"] = self.list
            
            if len(self.cal_list) == 4:
                if "%" in self.cal_list[-4] or "%" in self.cal_list[-2]:
                    if "%" in self.cal_list[-4]:
                        temp = self.cal_list[-4][0:len(self.cal_list[-4])-1]
                        temp = eval(temp + "/" + str(100) )
                        self.cal_list[-4] = str(temp)
                        temp = 0
                    
                    if "%" in self.cal_list[-2]:
                        if self.cal_list[-3] == "+" or self.cal_list[-3] == "-":
                            temp_2 = self.cal_list[-4]
                            rate = self.cal_list[-2][0:len(self.cal_list[-2])-1]
                            interest = eval((temp_2 + "*" + rate) + "/" + "100")
                            self.cal_list[-2] = str(interest)
                        if self.cal_list[-3] == "*" or self.cal_list[-3] == "/":
                            temp = self.cal_list[-2][0:len(self.cal_list[-2])-1] + "/" + "100"
                            self.cal_list[-2] = temp
                        
                        temp = 0
                        temp_2 = ""
                    
                
                self.temp = eval(self.cal_list[-4] + self.cal_list[-3] + self.cal_list[-2])
                self.l_display["text"] = str(self.temp)
                print("temp : ",self.temp)
                self.cal_list = []
                self.cal_list.append(str(self.temp))
                self.cal_list.append(self.c_opt)

root=Tk()
root.title("CALCULATOR_windows")
root.geometry("500x520")
root.minsize(500,520)
root.maxsize(500,520)
mycal=Calulator(root)
root.mainloop()
