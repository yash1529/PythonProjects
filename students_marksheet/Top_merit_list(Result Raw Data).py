#to print the merit list upto particular ranking defined
import re,sys


"""fetch data from list.bin"""



def extract_data():
    """To extract data from bin file"""
    with open("list.bin",mode="rb") as f:
        list=f.read()
        list=eval(list.decode())#decoded data
    return list

lst=extract_data()#list extracted from bin file


#and the list has been already sorted from highest to lowest(default)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def create_list(lst):
    """to extract names and percetage and alloted to respected list"""
    names=[]#list for names
    percetage=[]#list for percentage
    for x in range(len(lst)):
        names.append(lst[x][0])
        percetage.append(lst[x][3])
    
    return names,percetage

names,percentage=create_list(lst)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def remove_space(lst_names):
    """To remove extra whitespace from names in order to store it into excel file if needed"""
    new=lst_names.copy()
    for n in range(len(new)):
        temp=new.pop(n)#removed
        temp=temp.rstrip()#removed whitespace
        new.insert(n,temp)#inserted into original position
    return new

name_excel=remove_space(names)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lst=zip(names,percentage)
lst=list(lst)#converted into nested list

opt=input("Show result from highest or Lowest ?[H?L] :")
no=int(input("How many students : "))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if opt=="H" or opt=="h":
    print("Top %d students from higest to lowest:"%no)
    print()
    print("Rank\tNames\t\t\t -------------------------\t\tPercentage(%)")
    print("\n")
    for rank in range(no):
        print("{}.\t{} -------------------------\t\t{}".format(rank+1,lst[rank][0],lst[rank][1]))

elif opt=="l" or opt=="L":
    print("Top %d students from Lowest to Highest:"%no)
    print()
    print("Rank\tNames\t\t\t ------------------------- \t\tPercentage(%)")
    print("\n")
    for rank in range(no):
        print("{}.\t{} -------------------------\t\t{}".format(125-rank,lst[124-rank][0],lst[124-rank][1]))

else:
    print("Wrong input!")
    sys.exit()

cho=input("Do you want to create text file or excel sheet ? [T/E] :")
if cho=="T" or cho=="t":
    #creates text file
    with open("Top_merit_list.txt",mode="w") as f:
        f.write("List of Merit student\n")
        f.write("Rank\tNames\t\t\t ------------------------- \t\tPercentage(%)\n")
        f.write("\n")
        if opt=="H" or opt=="h":
            for rank in range(no):
                f.write("{}.\t{} -------------------------\t\t{}\n".format(rank+1,lst[rank][0],lst[rank][1])) 
        else:
            for rank in range(no): 
                f.write("{}.\t{} -------------------------\t\t{}\n".format(125-rank,lst[124-rank][0],lst[124-rank][1]))   

elif cho=="E" or cho=="e":
    #creates excel sheet
    from xlwt import Workbook
    wb=Workbook()
    sheet1=wb.add_sheet("Top_merit_list")
    sheet1.write(0,0,"List of Merit student")
    sheet1.write(1,0,"Rank")
    sheet1.write(1,1,"Names")
    sheet1.write(1,2,"Percentage(%)")
    if opt=="h" or opt=="H":
        for row in range(no):
            col=0
            while col<=2:
                sheet1.write(row+2,col,row+1)#rank
                col+=1
                sheet1.write(row+2,col,lst[row][0])#name
                col+=1
                sheet1.write(row+2,col,str(lst[row][1])+"%")#percentage
                col+=1

    else:
        for row in range(no):
            col=0
            while col<=2:
                sheet1.write(row+2,col,125-row)#rank
                col+=1
                sheet1.write(row+2,col,lst[124-row][0])#name
                col+=1
                sheet1.write(row+2,col,str(lst[124-row][1])+"%")#percentage
                col+=1
    wb.save("Top_merit_list.xls")

else:
    print("Wrong input!")
    sys.SystemExit()