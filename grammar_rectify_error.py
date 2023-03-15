####################        RECTIFICTAION OF GRAMMARTICAL ERROR IN A STRING     ##########################
from array import array#gloabal declaration

def str_to_arr(string):
    """ To convert string  in to array """
    arr=array("u",(x for x in string))
    arr.insert(0," ")#insert space
    #need to pop out "fullstop" @ the end of string as it is creating problem
    return arr

####################                         EXTRA_SPACE                        ###########################    
def extra_space(display):
    """To remove extra space between the strings"""
    i=0
    while i<len(display):
        if(display[i]==" " and display[i+1]==" "):
            j=i+1
            while display[j]==" ":
                display.pop(j)#pops out whitespace
            i-=1#need to reduce so that it doesn't gets out of range
        else:
            pass
        i+=1#increment in the value for outer while loop
    return display

###########################                CAPITAL LETTER                     ############################                
def cap_1st_letter(display):
    """ Converting into upper case if the first char of string at the start is lower case"""
    if ord(display[1]) in range(97,123):
        display[1]=chr(ord(display[1])-32)#converted into upper case
    else:pass
    def cap_fs(display):
        """ Converting into upper case if the first char after punctuation mark is lower case"""
        for i in range(len(display)-1):
            if display[i]=="." or display[i]=="," or display[i]=="?" or display[i]=="!":#punctuation marks
                if display[i+1]==" ":#space
                    if ord(display[i+2]) in range(97,123):# if i is in lower case ascii value
                        display[i+2]=chr(ord(display[i+2])-32)#converted into upper case
                    else:pass
                else:pass
            else:pass
        return display
    display=cap_fs(display)   
    return display

###################          PUNCTUATION WHITESPACE ERROR RECTIFICATION          #########################
def pun_error(display):
    """To remove whitespace found between string and punctuation mark"""
    i=0
    while i<len(display):
        if display[i]=="." or display[i]=="," or display[i]=="!" or display[i]=="?":#punctuation marks
            if display[i-1]==" ":#space
                display.pop(i-1)
            else:pass
        else:pass
        i+=1
    def pun_error2(display):
        """To add whitespace if there is not after punctuation marks"""
        i=0
        while i < len(display)-1:
            if display[i]=="." or display[i]=="," or display[i]=="!" or display[i]=="?":#punctuation marks
                if display[i+1]==" ":pass#if space is there then dont need to do anything
                else:
                    display.insert(i+1," ")
            i+=1
        return display
    display=pun_error2(display)
    display=cap_1st_letter(display)
    #need to invoke the above function bcuz after correction cases of char after punctuation will be lower
    return display

#####################              ARTICALS ERRORS RECTIFICATION             ##############################
def artical_error(display):
    """To rectify errors for 'an' and 'a' artical"""
    def a_artical(display):
        """To rectify error for 'a' artical """
        i=0
        while i <len(display)-1:
            if display[i-1]==" ":#space
                if display[i:i+2]==array("u",["a","n"]) or display[i:i+2]==array("u",["A","n"]):
                    if display[i+2]==" ":#space
                        if display[i+3] in vowels:pass
                        else:display.pop(i+1)# "an" becomes "a" bcuz its a consonant
                    else:pass
                else:pass
            else:pass
            i+=1
        return display

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    main execution    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    vowels=array("u",["A","a","E","e","I","i","O","o","U","u"])#array of vowels
    i=0
    while i < len(display)-1:
        if display[i-1]==" ":#space
            if display[i]=="a" or display[i]=="A":
                if display[i+1]==" ":#space
                    if display[i+2] in vowels:
                        display.insert(i+1,"n")# "a" becomes "an" bcuz its a vowel
                    else:pass
                else:pass
            if display[i:i+2]==array("u",["a","n"]) or display[i:i+2]==array("u",["A","n"]):
                display=a_artical(display)#if an is found in string
        else:pass
        i+=1
    return display

#######################              FIND & REPLACE SUBSTRING                ############################
def find_replace(display,find,replace):
    """"To find and replace if sub-string required by the user"""


    def find_fn(display_index,display,find,flag):
        """To find the old word which needs to be replaced by the new word"""
        i=display_index+1 #assigining as it too long to type ;)
        for k in find[:]:
            if ord(k)==ord(display[i]) or ord(k)==ord(display[i])+32:#in order to compare due to case sensitive
                 flag=True
            else:
                flag=False
                break
            i+=1
        return flag#return flag=true if word is found or else flag=False


    def pop_fn(display,find,display_index):
        """To pop out the old word """
        i=0
        while i < len(find):
            display.pop(display_index)
            i+=1
        return display


    def insert_fn(display,replace,display_index):
        """To insert new word in the place of old word"""
        i=0
        while i < len(replace):
            display.insert(display_index,replace[i])
            display_index+=1
            i+=1
        return display
    #~~~~~~~~~~~~~~~~~~~~~~~~~~           main programme flow            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    i=0
    while i < len(display):
        if display[i]==" ":#space
            if ord(display[i+1])==ord(find[0]) or ord(display[i+1])+32==ord(find[0]):#first char is found
                flag=False #becomes True if word is found
                flag=find_fn(i,display,find,flag)# i represents display_index
                if flag==True:# word has been found
                    i+=1
                    display=pop_fn(display,find,i)
                    display=insert_fn(display,replace,i)
                else:pass #no word is found
            else:pass
        else:pass
        i+=1
    display=cap_1st_letter(artical_error(display))#as the words are replaced their articals and initials are changed hence we need fix this error
    return display     

################################        RECORD of char,string         #############################################
def record(display):
    """To track record of words and char in a string"""
    withspace=len(display)
    withoutspace=0
    for i in display:#to count no of char without whitespaces
        if i==" ":#space
            pass
        else:withoutspace+=1 #add 1 if char is found
    
    """to count no of words in a string"""
    k=word=0
    flag=True #becomes false if no space is found
    for i in display :
        #count only when space no space is found
        if flag==False and display[k]==" ":
            word+=1
        #if a space if found take flag as true
        if display[k]==" ":#space
            flag=True
        else:
            flag=False
        k+=1
    return (withspace-1,withoutspace,word+1)
#need to "withspace-1" for whitespace as it is counting from start and there is space in the start of array
#also need to "word+1" bcuz it wont count the last word

#######################                *Main progarmme output*            ################################
string=input("Enter a string :\n")#user input
display=str_to_arr(string)#converted into array
display=extra_space(display)#removval of extra space
display=cap_1st_letter(display)#case converted into upper case after every punctuation mark
display=pun_error(display)#removed the whitespace found between punctuation marks and string
display=artical_error(display)#rectified the error for articals usage in string
find_swap=input("Do u want to replace an word ? [Y/N] : ")
if find_swap=="Y" or find_swap=="y":
    find=input("Enter a word to find : ")
    replace=input("Enter a word to replace in the place of '%s' : "%find)
    display=find_replace(display,find,replace)
else:pass
display.tolist()#converted into list
display="".join(display)#converted into string
print(display)
track=input("Do u want to know number of chr,string input ? [Y/N]: ")
if track=="Y" or "y":
    m=record(display)#invoking out the fuction
    print("Withspaces char : ",m[0])#no of char with spaces
    print("Withouspaces char : ",m[1])#no of char without spaces
    print("No.of words : ",m[2])#no of words in a string
else:pass