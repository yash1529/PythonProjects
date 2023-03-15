#to sort best of 6/5/4/3/2/1 subjects for all students or selected no of students
import sys
def extract_data():
    """To extract list from bin file"""
    with open("list.bin",mode="rb") as f:
        lst=f.read()
        lst=eval(lst.decode())
    #list contains(name,dict(marks),total,percentage)
    return lst

lst=extract_data()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_name_marks(lst):
    """To create a individual list for names,marks"""
    marks=[]#list for marks
    names=[]#list for names
    for x in range(len(lst)):
        names.append(lst[x][0])#names
        marks.append(lst[x][1])#marks
    return names,marks

names,dict_marks=extract_name_marks(lst)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sort_dict(marks):
    """to sort dict based on their marks"""
    for x in range(len(marks)):
        temp=marks.pop(x)#removes dict
        temp={code: marks for code, marks in sorted(temp.items(), key=lambda item: item[1],reverse=True)}
        marks.insert(x,temp)
    return marks
    
dict_marks=sort_dict(dict_marks)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def best_of(names,sub_marks,no):
    """To sort the students on their best of no of subjects"""
    sub_code=[]#subject code list
    score=[]#list of scores
    for x in sub_marks:
        temp_subcode=list(x.keys())#list of subject code
        sub_code.append(temp_subcode)
        temp_marks=list(x.values())#list of score
        score.append(temp_marks)
    
    def no_subject(sub_code,score,no):
        """To create a nested list of name,subjectcode and marks of particular no subjects defined by the user"""
        
        for x in range(len(names)):
            temp=sub_code.pop(x)#pops out list_subcode
            temp_2=[]#2nd temp list
            for pos in range(no):
                temp_2.append(temp[pos])
            sub_code.insert(x,temp_2)#defined no of subject_code has been added
        
        del(temp)
        del(temp_2)

        for x in range(len(names)):
            temp=score.pop(x)#pops out list_marks
            temp_2=[]#2nd temp list
            for pos in range(no):
                temp_2.append(temp[pos])
            score.insert(x,temp_2)#defined  no of subject_marks has been inserted
        
        del(temp)
        del(temp_2)

        return sub_code,score
    sub_code,score=no_subject(sub_code, score,no)

    def convert(lst):
        """To convert into nested list"""
        res=[]#new_list
        for el in lst:
            sub=el.split(",")
            res.append(sub)
        return res

    names=convert(names)
    new_lst=list(zip(names,sub_code,score))#nested list for names,subject code and marks

    return new_lst
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def merit_list(new_lst):
    """To get top no of results sorted based on total"""
    new_lst=sorted(new_lst,key=lambda pos:sum(pos[2]),reverse=True)
    return new_lst

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def convert_format(lst):
    """To convert sub elements of list into list format bcuz tuple does not have append attribute"""
    for x in range(len(lst)):
        temp=lst.pop(x)#removes the tuple element
        temp=list(temp)#converts into list format
        lst.insert(x,temp)
    return lst

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def percentage(lst):
    """To calculate Total and percentage"""
    for pos in range(len(lst)):
        total=sum(lst[pos][2])#sum of all subjects
        per=(total/(len(lst[pos][2])*100))*100# calculate_percentage
        per=round(per,2)#round off upto 2numbers after decimal point
        lst[pos].append([total])
        lst[pos].append([per])
    return lst    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find_max_size(names):
    """to find the max size character"""
    x=len(max(names,key=len))
    
    return x
chr_max_size=find_max_size(names)


def manage_space(name,size_max_name):
    """In order to give equal space to names """
    max_len=size_max_name
    name=name+(max_len-len(name))*" "
    return name 



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def display(lst,no_students,best_of):
    """To display final result"""
    print("Rank\tName\t\t\tBest of {} Subjects".format(best_of),end="")
    for x in range(best_of):
        #to manage tab space
        print("\t",end="")
    print("Total\tPercentage(%)")
    print("\n")
    for x in range(no_students):
        name=manage_space(lst[x][0][0], chr_max_size)#after managing space for name
        print("{}\t{}".format(x+1,name),end="\t")#rank and names
        for code,marks in zip(lst[x][1],lst[x][2]):
            #to print subject code and marks 
            print("{}:{}".format(code,marks),end="\t")
        print("\t",end="")
        print(lst[x][3][0],end="\t")#total
        print(lst[x][4][0],end="%")#percentage
        print()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~main Program~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Total no of Subjects = 6")
print("enter 'all' inorder to get best of 6 or enter between '1 to 6' to acquire best of selected number of subject's result\n")
no_of_sub=input("How many Subjects : ")
print("Total no of students : 125")
no_people=int(input("No of students? :"))
if eval(no_of_sub) in range(1,7):
    x=merit_list(best_of(names, dict_marks, int(no_of_sub)))
    x=convert_format(x)
    final_lst=percentage(x)
    display(final_lst, no_people, int(no_of_sub))

elif no_of_sub=="all":
    x=merit_list(best_of(names, dict_marks,6))
    x=convert_format(x)
    final_lst=percentage(x)
    display(final_lst, no_people,6)

else:
    print("Invalid Input!")
    sys.exit()

cho=input("Do you want to import this data into Text file or Excel sheet?[T/E] :")
if cho=="T" or cho=="t":
    with open("best_of_Result.txt",mode="w") as f:
        f.write("Best of {} Subjects of top {} Student:\n".format(no_of_sub,no_people))
        f.write("\n")
        f.write("Rank\tNames\t\t\t")
        f.write("Best of {} Subjects [subject_code:Marks]".format(no_of_sub))
        f.write("\t\t\t")
        f.write("Total\tPercentage(%)\n")
        for x in range(no_people):
            f.write("%d\t"%(x+1))#rank
            name=manage_space(final_lst[x][0][0], chr_max_size)#after managing space for name
            f.write("{}\t".format(name))#name
            for code,marks in zip(final_lst[x][1],final_lst[x][2]):
                #to print subject code and marks 
                f.write("{}:{}".format(code,marks))
                f.write("\t")
            #manage space
            if no_of_sub=="6" or no_of_sub=="all":
                f.write("\t")
            elif no_of_sub=="5":
                f.write("\t\t")
            elif no_of_sub=="4":
                f.write("\t\t\t")
            elif no_of_sub=="3":
                f.write("\t\t\t\t")
            elif no_of_sub=="2":
                f.write("\t\t\t\t\t")
            elif no_of_sub=="1":
                f.write("\t\t\t\t\t\t")

            f.write("{}\t".format(final_lst[x][3][0]))#total
            f.write("{}%".format(final_lst[x][4][0]))#percentage
            f.write("\n")

elif cho=="E" or cho=="e":
    from xlwt import Workbook
    wb=Workbook()
    sheet1=wb.add_sheet("Best of Subjects")
    sheet1.write(0,0,"Best of {} Subjects for Top {} Students".format(str(no_of_sub),str(no_people)))
    sheet1.write(1,0,"Rank")
    sheet1.write(1,1,"List of Names")
    
    if no_of_sub=="all":
        no_of_sub=6
    
    i=0
    while i < int(no_of_sub)*2:
        #to print cols for no of subject code and marks
        sheet1.write(1,i+2,"Subjec_code")
        i+=1
        sheet1.write(1,i+2,"Marks")
        i+=1
    sheet1.write(1,i+2,"Total")

    i+=1
    sheet1.write(1,i+2,"Percentage(%)")
    x=(int(no_of_sub)*2)+4#total no of cols
    for row in range(no_people):
        col=0
        while col < x:
            sheet1.write(row+2,col,"%d"%(row+1))#rank
            col+=1
            sheet1.write(row+2,col,"{}".format(final_lst[row][0][0]))#name
            col+=1
            for code,mark in zip(final_lst[row][1],final_lst[row][2]):
                #to write subject_code and their marks 
                sheet1.write(row+2,col,"{}".format(code))#subject code
                col+=1
                sheet1.write(row+2,col,"{}".format(mark))#marks
                col+=1
            sheet1.write(row+2,col,"{}".format(final_lst[row][3][0]))#total
            col+=1
            sheet1.write(row+2,col,"{}%".format(str(final_lst[row][4][0])))#percentage
            col+=1

    wb.save("Bestofsubject.xls")
    while True:
        opt=input("Do You want to create a new excel sheet for Creating new Best of Subjects?[Y/N]:")
        if opt=="Y" or opt=="y":
            print("Total no of Subjects = 6")
            print("enter 'all' inorder to get best of 6 or enter between '1 to 6' to acquire best of selected number of subject's result\n")
            
            
            no_of_sub=input("How many Subjects : ")
            check=["1","2","3","4","5","6","all"]
            if no_of_sub in check:
                pass
            else:
                print("Wrong input!")
                sys.exit()
                
            if no_of_sub=="all":
                no_of_sub=="6"

            print("Total no of students : 125")
            no_people=int(input("No of students? :"))
            x=merit_list(best_of(names, dict_marks, int(no_of_sub)))
            x=convert_format(x)
            final_lst=percentage(x)

            sheet=wb.add_sheet("Best of {} Subjects".format(str(no_of_sub)))
            sheet.write(0,0,"Best of {} Subjects for Top {} Students".format(no_of_sub,str(no_people)))
            sheet.write(1,0,"Rank")
            sheet.write(1,1,"List of Names")
            
            if no_of_sub=="all":
                no_of_sub=6
            
            i=0
            while i < int(no_of_sub)*2:
                #to print cols for no of subject code and marks
                sheet.write(1,i+2,"Subjec_code")
                i+=1
                sheet.write(1,i+2,"Marks")
                i+=1
            sheet.write(1,i+2,"Total")

            i+=1
            sheet.write(1,i+2,"Percentage(%)")
            x=(int(no_of_sub)*2)+4#total no of cols
            for row in range(no_people):
                col=0
                while col < x:
                    sheet.write(row+2,col,"%d"%(row+1))#rank
                    col+=1
                    sheet.write(row+2,col,"{}".format(final_lst[row][0][0]))#name
                    col+=1
                    for code,mark in zip(final_lst[row][1],final_lst[row][2]):
                        #to write subject_code and their marks 
                        sheet.write(row+2,col,"{}".format(code))#subject code
                        col+=1
                        sheet.write(row+2,col,"{}".format(mark))#marks
                        col+=1
                    sheet.write(row+2,col,"{}".format(final_lst[row][3][0]))#total
                    col+=1
                    sheet.write(row+2,col,"{}%".format(str(final_lst[row][4][0])))#percentage
                    col+=1

            wb.save("Bestofsubject.xls")

        elif opt=="N" or opt=="n":
            break
        else:
            print("Wrong input!")
            break
else:
    print("Wrong input!")
    sys.exit()
sys.exit()