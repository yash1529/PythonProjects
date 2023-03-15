
import xlrd
path="D://Python_vs_code//Book1.xls"

excel_workbook=xlrd.open_workbook(path)
excel_worksheet=excel_workbook.sheet_by_index(0)#worksheet no start with 0,1,2,3 ,..

#x=excel_worksheet.cell_value(4,0)
NO_OF_ROWS=excel_worksheet.nrows #no of rows
NO_OF_COLUMNS=excel_worksheet.ncols #no of columns



def sort_data():
    """to differentiate the students payment status"""
    temp=[]#for nested list 
    PAID=[]#list for paid students
    UNPAID=[]#list for unpaid students
    for row in range(1,NO_OF_ROWS):
        if excel_worksheet.cell_value(row,2)=="UNPAID":
            for col in range(NO_OF_COLUMNS):
                temp.append(excel_worksheet.cell_value(row,col))
            UNPAID.append(temp)
        else:
            for col in range(NO_OF_COLUMNS):
                temp.append(excel_worksheet.cell_value(row,col))
            PAID.append(temp)
        temp=[]#empty

    return PAID,UNPAID


def excel_file(asked,status):
    """To create excel file"""
    from xlwt import Workbook
    wb=Workbook()
    sheet1=wb.add_sheet("status")#sheet name
    temp=("NAME","STD","PAYMENT STATUS","CONTACT NO","CONCESSION","CONCESSION AMT","FEES SUBSCRIPTION","PAY MODE","AMOUNT","FEES INFO")
    for col in range(NO_OF_COLUMNS):
        sheet1.write(0,col,temp[col])
    
    for row in range(len(status)):
        for col in range(NO_OF_COLUMNS):
            sheet1.write(row+1,col,str(status[row][col]))

    wb.save("{} fees.xls".format(asked))
    


def main():
    """main function"""
  
    PAID,UNPAID=sort_data()
    ask=input("Do u want to create paid or unpaid list? [P/U] : ")
    #PAID=P or  UNPAID=U
    if ask=="P" or ask=="p":
        excel_file("PAID",PAID)
    elif ask=="U" or ask=="u":
        excel_file("UNPAID",UNPAID)

if __name__=="__main__":
    main()
