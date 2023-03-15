#to check whether the mail id is valid or not
######################                          USER ID                    ##############################

def fst_char(mail_id):
    """To check whether the 1st character of user id is alphabet or not"""
    if ord(mail_id[0]) in range(65,91) or ord(mail_id[0]) in range(97,123):
        error=None
    else:
        error="1st character of user_id is an alphabet."
    return error


def symbol_at(mail_id):
    """To check whether there is @ symbol or not in the mail id"""
    if mail_id.find("@")!=-1:
        error=None
    else:
        error="There is no @ symbol in the above mail id hence its not a valid email id."
    return error


def special_char(mail_id):
    """To chek whether there are other special character rather then ".","_" and "a" """
    from itertools import chain
    range_=tuple(chain(range(64,91),range(97,123),range(48,58),range(46,47),range(95,96)))
    #concatination of both the cases of letters, 0-9 numbers, few special symbols like ".","_","@"
    for i in mail_id:
        if ord(i) in range_:
            error=None # i.e no errors
        else:
            error="{} is a special symbol which should not be included in mail id.".format(i)
            break
    return error


def check_before_at(mail_id):
    """To check whether there is special symbol before @"""
    from itertools import chain
    range_=tuple(chain(range(65,91),range(97,123),range(48,58)))
    #concatination of both the cases of letters, 0-9   1 digit number
    pos=mail_id.find("@")
    if ord(mail_id[pos-1]) in range_:
        error=None# i.e no errors
    else:
        error="%s symbol should not be there before @."%mail_id[pos-1]
    return error


def fullstop_fn(mail_id):
    """To check fullstop is there or not"""
    pos=mail_id.rfind(".")
    i=mail_id.rfind("@")
    if pos!=-1:
        #full stop is there in the mail id
        if pos > i:
            error=None
        else:
            error=" '.' should be placed after @ symbol and domain name"
    else:
        error=" '.' is not there hence extension cannot be identified and its a invalid mail id!"
    return error


def domain(mail_id):
    """To check whether the domain name is correct or not and it should be of atleat 3 letters"""
    pos=mail_id.find(".")
    i=mail_id.find("@")
    from itertools import chain
    range_=chain(range(65,91),range(97,123))
    if fullstop_fn(mail_id)==None:#to check fullstop is there or not
        if pos-i >=4:#
            if ord(mail_id[i+1]) in range_:
                error=None
                return error
            else:
                #first char should be an alphabet
                error="domain name should start with alphabets not numbers"
                return error
        else:
            error="domain name should be of atleast 3 characters"
            return error
    else:
        error=fullstop_fn(mail_id)#calling the fuction in order to check whether fullstop exist or not
        return error


def extension_fn(mail_id):
    """To check whether the extension name is correct or not"""
    if fullstop_fn(mail_id)==None:
        z=mail_id.rfind(".")
        count=0
        pos=z+1#next character after "."
        while pos<=len(mail_id)-1:
            count+=1
            pos+=1

        if count>=2:
            error=None
        else:
            error="Extension name should of atleast 2 chararcter"
    else:
        #fullstop is not there
        error=fullstop_fn(mail_id)
    return error
    
###########################       OUTPUT        ####################################
g_address=input("Enter your mail id : ")
print(fst_char(g_address))
print(symbol_at(g_address))
print(special_char(g_address))
print(check_before_at(g_address))
print(domain(g_address))
print(extension_fn(g_address))
if fst_char(g_address)==None:
    if symbol_at(g_address)==None:
        if special_char(g_address)==None:
            if check_before_at(g_address)==None:
                if domain(g_address)==None:
                    if extension_fn(g_address)==None:
                        print("Your mail_id is valid !")
                    else:print("Please rectify the above error to make ur email id valid!")
                else:print("Please rectify the above error to make ur email id valid!")
            else:print("Please rectify the above error to make ur email id valid!")
        else:print("Please rectify the above error to make ur email id valid!")
    else:print("Please rectify the above error to make ur email id valid!")
else:print("Please rectify the above error to make ur email id valid!")
