#to extract data from the given txt(Result Raw Data.txt) file as per our need.
import re,sys
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cal_percentage():
    with open("Result Raw Data.txt",mode="r") as f:
        f.readline()#skip the line
        f.readline()#skip the line
        
        x=f.read()

        #lst_name=re.split(r"\t",x)
        lst_name=re.findall("\d+\s+\w\s+(\w+\s+\w+\s+\w*\s*)\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\w+",x)
        lst_marks=re.findall("\d+\s+\w\s+\w+\s+\w+\s+\w*\s*\d+\s+(\d+)\s+\w+\s+\d+\s+(\d+)\s+\w+\s+\d+\s+(\d+)\s+\w+\s+\d+\s+(\d+)\s+\w+\s+\d+\s+(\d+)\s+\w+\s+\d+\s+(\d+)\s+\w+\s+\w+",x)
        lst_rollno=re.findall("(\d+)\s+\w\s+\w+\s+\w+\s+\w*\s*\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\d+\s+\d+\s+\w+\s+\w+",x)
        lst_sub_code=re.findall("\d+\s+\w\s+\w+\s+\w+\s+\w*\s*(\d{3})\s+\d+\s+\w+\s+(\d+)\s+\d+\s+\w+\s+(\d+)\s+\d+\s+\w+\s+(\d+)\s+\d+\s+\w+\s+(\d+)\s+\d+\s+\w+\s+(\d+)\s+\d+\s+\w+\s+\w+",x)
        

        convert=[]#nested list converted into int format
        """need to convert nested list format into int_format"""
        for marks in lst_marks:
            x=marks#tuple format and inside marks are in string format
            int_form=[]
            for no in x:
                int_form.append(eval(no))
            convert.append(int_form)
            
        def cal(new_lst):
            """in order to calulate percenatge of nested list"""
            percentage=[]#list for percentage of students:
            for x in new_lst:
                #round(0,2) this method helps tp reduce the number upto 2 after decimal
                per=round((sum(x)/600)*100,2)
                percentage.append(per)#need to reduce it to 2 digit after decimal point
            return percentage
        
                    
        lst_percentage=cal(convert)#invoking the function
        return lst_percentage,lst_name,convert,lst_rollno,lst_sub_code

per_lst,lst_name,lst_marks,lst_rollno,lst_sub_code=cal_percentage()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def remove_space(lst_name):
    """To remove \t from the names :"""
    
    for x in range(len(lst_name)):
        temp=list(lst_name.pop(x))#removal of element
        temp="".join(temp)#converted into string
        if "\t10" in temp:
            temp=temp.replace("\t10","")
            lst_name.insert(x,temp)
        else:
            temp=temp.replace("\t","")
            lst_name.insert(x,temp)

    return lst_name

lst_name=remove_space(lst_name)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def find_max_size(names):
    """to find the max size character"""
    x=len(max(names,key=len))
    
    return x

size_max_name=find_max_size(lst_name)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def manage_space(names,size_max_name):
    """In order to give equal space to all the names """
    max_len=size_max_name
    new_lst=[]#new empty list
    for x in range(len(names)):
        temp=names.pop(x)#removes the element
        temp=temp+(max_len-len(temp))*" "
        names.insert(x,temp)
    return names

lst_name=manage_space(lst_name,size_max_name)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def merge_sub_code_marks(lst_sub_code,lst_marks):
    """To merge subject code and subject marks and convert into dict format"""
    new_lst=[]#empty lst
    for code,marks in zip(lst_sub_code,lst_marks):
        """this helps to fetch values of multiple list at the same time while iterating"""
        x=zip(code,marks)
        x=dict(x)
        new_lst.append(x)
    return new_lst

merged=merge_sub_code_marks(lst_sub_code,lst_marks)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sum_nested_lst(lst_marks):
    """To find the total marks of a student  from nested list"""
    total=[]#empty list for sum of given nested list
    for x in lst_marks:
        total.append(sum(x))
    return total

lst_sum_marks=sum_nested_lst(lst_marks)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def convert_int_format_rollno(lst_rollno):
    """to Convert string format into int_format"""
    new_lst=[]#new empty lst for rollno
    for x in lst_rollno:
        new_lst.append(eval(x))
    return new_lst

lst_rollno=convert_int_format_rollno(lst_rollno)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def nested_lst(lst_name,merged,lst_sum_marks,per_lst):
    """To create a nested_list of marks,percentage,rollno,total"""
    
    new_lst=[]#need to merge all the elements of multiple list one by one

    for x in range(len(per_lst)):
        temp=[]#temperory list in order to create a nested list
        temp.append(lst_name[x])
        temp.append(merged[x])
        temp.append(lst_sum_marks[x])
        temp.append(per_lst[x])
        new_lst.append(temp)
    return new_lst
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pos=3#to sort on the bases of 4th element
def pos_input(pos):
    #to give position to takeper
    return pos 

 
def takeper(elem):
    """to sort nested list base on percentage"""
    return elem[pos_input(pos)]

lst=nested_lst(lst_name,merged,lst_sum_marks,per_lst)#invoking function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bin_file(lst):
    """to create an object and save it as bin file for other folders to read """
    temp=lst
    temp=temp.sort(key=takeper,reverse=True)#default sorting is from highest to lowest
    temp=str(lst)
    with open("list.bin",mode="wb") as f:
        f.write(temp.encode())

bin_file(lst)#bin.file hasbeen created



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Show % from Higest or Lowest [H/L]: ")
opt=input("Your choice : ")
print("\n")
if opt=="H" or opt=="h":
    order="Decending"
    lst.sort(key=takeper,reverse=True)#sorted based on highest to lowest %
   
    count=1
    for name,marks,total,per in lst:
        print("{}. {}\t\t{}\t{}\t{}%".format(count,name,marks,total,per))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        count+=1
        
elif opt=="L" or opt=="l":
    order="Ascending"
    lst.sort(key=takeper)
    count=1
    for name,marks,total,per in lst:
        print("{}. {}\t\t{}\t{}\t{}%".format(count,name,marks,total,per))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        count+=1
else:
    
    print("Wrong option entered!")
    sys.exit()

cho=input("Do u Want to create a text file  or excel sheet?[T/E] :")
if cho=="T" or cho=="t":
    with open("sorted_basedon%.txt",mode="w") as f:
        f.write("Names sorted in {} order based on %\n".format(order))
        f.write("Rank\tNames\t\t\tSubject Code : marks\t\t\t\tTotal\tPercentage\n")
        f.write("\n")
        count=1
        for name,marks,total,per in lst:
            f.write("{}. {}\t\t{}\t{}\t{}%\n".format(count,name,marks,total,per))
            f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            count+=1

elif cho=="E" or cho=="e":
    #to print marksheet in excel sheet using python:
    from xlwt import Workbook
    import re
    wb=Workbook()
    sheet1=wb.add_sheet("Student_list")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def headings(sheet1):
        sheet1.write(0,0,"List of Students from higest to lowest")
        """to create heading folder at the start"""
        sheet1.write(1,0,"Rank")
        sheet1.write(1,1,"Student's Name")
        col=2
        while col<14:
            sheet1.write(1,col,"Subject Code")
            col+=1
            sheet1.write(1,col,"Marks")
            col+=1
        sheet1.write(1,col,"Total")
        sheet1.write(1,col+1,"Percentage (%)")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def extract_data(lst,opt):
        """to extract ranks,names,marks,subjectcode,percentage,total from pervious sorted list"""
        #rank=re.findall(r"(\d+).",raw_data)#list of ranks(incomplete)
        if opt=="h" or opt=="H":
            #list of rank from highest to lowest order
            rank=list(range(1,126))#list of ranks
            #list of rank from lowest to highest
        else:
            rank=list(range(125,0,-1))
            
        names=[]#list of names
        subcode_marks=[]#list of subcode and marks
        per=[]#list of percentage
        total=[]#list of total
        for n,m,t,p in lst:
            names.append(n)
            subcode_marks.append(m)
            total.append(t)
            per.append(p)

        return rank,names,subcode_marks,total,per

    

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def remove_space(names):
        """To remove extra space from names"""
        for x in range(len(names)):
            temp=names.pop(x)#removed from list
            temp=temp.rstrip()#removes extra whitespace
            names.insert(x,temp)

        return names

     #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
    headings(sheet1)#to create heading folder at the start
    rank,names,subcode_marks,total,per=extract_data(lst,opt)#to extract particular data from the raw_data
    
    names=remove_space(names)#removed extra whitespace
    
    
    def upload(sheet1,rank,names,subcode_marks,total,per):
        """To upload data in excel sheet"""
        lst=[rank,names,subcode_marks,total,per]
        row=2
        while row<127:
            col=0
           
            while col<16:
              
                sheet1.write(row,col,lst[0][row-2])#rank
                col+=1#col=1
                sheet1.write(row,col,lst[1][row-2])#name
                col+=1#col=2
                dict=lst[2][row-2]#dict of marks and their subject code of a single student
                for code,marks in dict.items():
                    sheet1.write(row,col,code)#subject code
                    col+=1#code=3
                    sheet1.write(row,col,marks)#subject marks
                    col+=1#code=4
                #col=14
                sheet1.write(row,col,lst[3][row-2])#total
               
                col+=1#col=15
                sheet1.write(row,col,str(lst[4][row-2])+"%")#percentage
                col+=1
            row+=1#outerloop
                
    upload(sheet1,rank,names,subcode_marks,total,per)
    wb.save("Raw_result.xls")


else:
    sys.exit()
