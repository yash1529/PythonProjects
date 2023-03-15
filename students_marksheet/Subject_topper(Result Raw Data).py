#to find subject wise topper:
import sys
def extract_list():
    """To extract data from bin file"""
    with open("list.bin",mode="rb") as f:
        lst=f.read()
        lst=lst.decode()
        lst=eval(lst)
    return lst

lst=extract_list()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_name_marks(lst):
    name=[]#list for names
    marks=[]#list for marks

    for x in range(len(lst)):
        name.append(lst[x][0])
        marks.append(lst[x][1])
    
    return name,marks

name,marks=extract_name_marks(lst)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sort(sub_code,name,marks):
    """sorting based on subject code"""
    lst_marks=[]#list of marks for particular subject
    for x in range(len(name)):
        lst_marks.append(marks[x][sub_code])
    
    merged=list(zip(name,lst_marks))#nested list for names and their marks
    return merged

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Subject Topper List :")
sub_code=input("Enter subject code : ")
opt=input("Show result from Highest or lowest?[H/L]: ")
if opt=="H" or opt=="h":
    lst=sort(sub_code, name, marks)#nested list for marks and names
    lst=sorted(lst,key=lambda pos:pos[1],reverse=True)#sorted listed based on marks of particular subject code

    print("Rank\tNames\t\t\tMarks In %s Subject"%sub_code)
    for x in range(len(lst)):
        print("{}.\t{}\t{}".format(x+1,lst[x][0],lst[x][1]))
elif opt=="L" or opt=="l":
    lst=sort(sub_code, name, marks)#nested list for marks and names
    lst=sorted(lst,key=lambda pos:pos[1])#sorted listed based on marks of particular subject code
    print("Rank\tNames\t\t\tMarks In %s Subject"%sub_code)
    for x in range(len(lst)):
        print("{}.\t{}\t{}".format(125-x,lst[x][0],lst[x][1]))
else:
    print("Wrong input!")
    sys.SystemExit()


cho=input("Do u want to import this list into text file or excel sheet?[T/E]: ")
if cho=="T" or cho=="t":
    with open("Subject_topper.txt",mode="w") as f:
        f.write("\t*Subject topper*\n")
        f.write("\n\n")
        f.write("Rank\tNames\t\t\tMarks In %s Subject\n"%sub_code)
        if opt=="h" or opt=="H":  
            count=1 
            for n,m in lst:
                f.write("{}.\t{}\t\t{}\n".format(count,n,m))    
                count+=1
        else:
             count=125
             for n,m in lst:
                f.write("{}.\t{}\t\t{}\n".format(count,n,m))    
                count-=1

elif cho=="E" or cho=="e":
    #to make excel sheet:
    from xlwt import Workbook
    wb=Workbook()
    sheet1=wb.add_sheet("Subject_Topper")
    sheet1.write(0,0,"List of Student's Rank as per Subject code :%s"%sub_code)   
    sheet1.write(1,0,"Rank")
    sheet1.write(1,1,"Names")
    sheet1.write(1,2,"Marks")
    
    if opt=="h" or opt=="H":
        rank=1
        for row in range(len(lst)):
            col=0
            while col<=2:
                sheet1.write(row+2,col,rank)#rank
                col+=1
                sheet1.write(row+2,col,lst[row][0])#name
                col+=1
                sheet1.write(row+2,col,lst[row][1])#marks
                col+=1
            rank+=1
        
    else:
        rank=125
        for row in range(len(lst)):
            col=0
            while col<=2:
                sheet1.write(row+2,col,rank)#rank
                col+=1
                sheet1.write(row+2,col,lst[row][0])#name
                col+=1
                sheet1.write(row+2,col,lst[row][1])#marks
                col+=1
            rank-=1
        
    wb.save("Subject_topper.xls")
else:

    print("Wrong input!")
    sys.SystemExit()