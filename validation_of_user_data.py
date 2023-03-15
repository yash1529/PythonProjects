#validation of data given by the user
#########################                           User's name                   ############################             
def name_fn(id_name):
    """To check wehther given string contains name only alphabets or not"""
    id_name=id_name.strip()#strips out extra space from both the ends if found
    flag=True#becomes false if anything other then alphabets are found
    error=[]#empty list for counting errors in input
    from itertools import chain
    range_=tuple(chain(range(65,91),range(97,123)))#combined list of all upper_lower case alphabets
    for i in range(len(id_name)):
        if ord(id_name[i]) in range_:
            flag=True
            #no error i.e all inputs are alphabets
        else:
            flag=False
            error.append(id_name[i])#adds up the characters which are not alphabets
         # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ final 
    if flag==True: 
        pass#input is correct!
    else:
        error=",".join(error)
        print("%s are not alphabets! Please rectify it!"%error)#shows the error for invalid input

    return id_name
##########################################################################
############################                User's address             ############################
#do u really need to check address of user as it contains various characters so i think theres really no need to check it
def address_fn(user_add):
    """To verify errors in address of the user's input"""
    flag=True#becomes false if error is found
    for i in range(len(user_add)):
        if ord(user_add[i]) in range(32,123):
            flag=True
            #no error i.e all inputs are alpha-numeric
        else:
            flag=False
            error.append(user_add[i])#adds up the characters which are not alphabets
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  final
    if flag==True:
        pass#input is correct no errors found!
    else:
        error=",".join(error)
        print("%s are not alphabets! Please rectify it!"%error)#shows the error for invalid input
    return user_add
########################################################################

def p_num_fn(number):
    def extra_space(display):
        """To remove extra space between the strings"""
        i=0
        while i<len(display):
            if display[i]==" ":
                while display[i]==" ":
                    display.pop(i)#pops out whitespace
                    i-=1#need to reduce so that it doesn't gets out of range
            else:pass
            i+=1#increment in the value for outer while loop
        return display
    from array import array
    display=array("u",(x for x in number))#converting into array
    number=extra_space(display)#removed extra space
    number.tolist()#converted into list
    number="".join(number)#converted into string
    """To verify user's phone number :"""
    flag=True#becomes false if error is found
    error=[]#empty list for error detection
    for i in range(len(number)):
        if ord(number[i]) in range(48,58):
            flag=True#range of all single digit from 0-9
        else:
            flag=False
            error.append(number[i])#adds up the characters which are not numbers
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if flag==True:pass#no errors are found
    else:
        error=",".join(error)
        print("%s are not numbers! Please rectify it!"%error)#shows the error for invalid input
    return number
##########################                       output                         ############################
name=input("Enter your name : ")
id_name=name_fn(name)#invoking the function
address=input("Enter your address : ")
user_add=address_fn(address)
p_number=input("Enter your phone number : ")
phone_number=p_num_fn(p_number)
import gmail_verify


