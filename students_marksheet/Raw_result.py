#to print marksheet in excel sheet using python:
from xlwt import Workbook
import re
wb=Workbook()
sheet1=wb.add_sheet("Student_list")

with open("sorted_basedon%.txt",mode="r") as f:
    #skipl line
    f.readline()
    f.readline()
    f.readline()
    raw_data=f.read()
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
def extract_data(raw_data):
    """to extract ranks,names,marks,subjectcode,percentage,total"""
    rank=re.findall(r"(\d+).",raw_data)#list of ranks(incomplete)
    #rank=list(range(1,126))#list of ranks
    names=re.findall(r"[A-Z]+\s+[A-Z]+\s+[A-Z]*\s*",raw_data)#list of names
    subcode_marks=re.findall(r"({.*})",raw_data)#list of subcode and marks
    per=re.findall(r"\d\d.\d\d*%",raw_data)#list of percentage
    total=re.findall(r"\s+(\d\d\d)\s+",raw_data)#list of total

    return rank,names,subcode_marks,total,per
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def remove_space(names):
    """To remove extra space from names"""
    for x in range(len(names)):
        temp=list(names.pop(x))#removed from list
        temp="".join(temp)#converted into string
        temp=temp.replace("\t\t","")#removes\t\t
        temp=temp.rstrip()#removes extra whitespace
        names.insert(x,temp)

    return names

 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def convert_format(subcode_marks):
    """To convert string format into dict format"""
    for x in range(len(subcode_marks)):
        temp=subcode_marks.pop(x)#removed
        temp=eval(temp)#converted int0 dict
        subcode_marks.insert(x,temp)#inserted at its original position
    return subcode_marks

    
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
headings(sheet1)#to create heading folder at the start
rank,names,subcode_marks,total,per=extract_data(raw_data)#to extract particular data from the raw_data
names=remove_space(names)#removed extra whitespace
subcode_marks=convert_format(subcode_marks)#format convert into dict

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
            sheet1.write(row,col,lst[4][row-2])#percentage
            col+=1
        row+=1#outerloop
            
upload(sheet1,rank,names,subcode_marks,total,per)
wb.save("Raw_result.xls")

