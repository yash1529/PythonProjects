#to check the status of employee
from datetime import *

import re
def extract_data():
    with open("Employees_Date_of_joininig.txt",mode="r") as f:
        raw=f.read()
    data=re.findall(r"\d+\s+\w+\s+(\d+\W\d+\W\d+)\s+\d+\W\d+\W\d+",raw)
    return data

data=extract_data()

def status_check(lst):
    """To check the status of an employee"""
    status=[]#empty list for status
    current_date=date.today()#current date
    for x in lst:
        temp=x.split("-")
        DOJ=date(eval(temp[2]),eval(temp[1]),eval(temp[0]))
        diff=current_date-DOJ#difference betwen 2 dates
        months,days=divmod(diff.days,30)#to find difference in months
        if months>=6:
            status.append("Permanant")
        else:
            status.append("Temporary")
    return (status)

status=status_check(data)

def append_status(status):
    """To append status in the exisiting file"""
    with open("Employees_Date_of_joininig.txt",mode="r") as f:
        temp=f.readlines()
        f.seek(0)#
        x=f.read()#skip

        #create a backupfile for original data
        bak=open("Employees_Date_of_joininig.bak",mode="w")
        bak.write(x)
        bak.close()

    with open("Employees_Date_of_joininig.txt",mode="w") as f:
        f.write(temp[0])#heading
        for x in range(len(status)):
            if temp[x+1].find("Permanant")==-1 and temp[x+1].find("Temporary")==-1:
                #not found
                f.write(temp[x+1].rstrip()+"\t"+status[x]+"\n")
                #ask how its working instead of temp[x+1].find("Permanant") and temp[x+1].find("Temporary") ==-1:
            else:
                f.write(temp[x+1].replace("Permanant"or"Temporary",status[x]))
                
append_status(status)






        
