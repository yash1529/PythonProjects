#to create a login credits interface:
import sys
def OTP_generate(id):
    import random
    from twilio.rest import Client
    ########################    Get ur phone no in order to send it for reset of password    ####################
    with open("register.txt",mode="r")as f:
        dict=eval(f.readline())#whole dict
        key=dict[id]#generates phone no and password of a particular id
        new_key=tuple(key)#gets key for the nested dict i.e password as key 
        phone_no=key[new_key[0]]#gets the phone no of user specified


    ####################################################################################
    otp=random.randint(1000000,10000000)#genrate otp
    account_sid="AC98ee2c479d8df2dd5b73573046042b0f"
    auth_token="03675a9d9e4ac3ee3d171fd733aea567"
    client=Client(account_sid,auth_token)
    message=client.messages.create(
        body="YYoour OTP to reset ur password is: "+str(otp),
        from_="+13203145246",
        to=phone_no,
    
    )
    print("Check Your phone to reset Your password by given otp!")
    with open("otp.txt",mode="w") as f:
        f.write("{}".format(str(otp)))

def merge_convert(dict,newid):
    """convert str format into dictionary format and also merge with exisiting dict"""
    code=input("Enter password : ")
    phno=input("Enter phone no : ")
    dict.update({newid:{code:phno}})
    with open("register.txt",mode="w")as f:
        dict=str(dict)
        f.write(dict)

def register(m):
    """To register the new entries and their passcode"""
    if m=="a+":
        with open("register.txt",mode=m) as f:
            import ast
            f.seek(0)
            x=f.readline()#in str format
            x=ast.literal_eval(x)#converted into dict format
            id=input("Enter id : ")
            if check_id(id)==0:
                """new id """
                merge_convert(x,id)
            else:
                """it already exist in the dictonary"""
                print("Id already registered! plz make use of new id")
                sys.exit()

            
    else:
        with open("register.txt",mode=m) as f:
            dict={}#empty dictionary
            n=int(input("Enter no of entries : "))
            for x in range(n):
                k=input("Enter id : ")
                v=input("Enter password : ")
                phno=input("Enter phone no : ")
                phno="+91"+phno
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                dict.update({k:{v:phno}})
            f.write("{}".format(dict))
        
def check_id(id):
    """To check validity of id"""
    with open("register.txt",mode="r") as f:
        found=0# default value false
        lst=eval(f.readline())
        if id in lst:
            found=1
        else:
            found=0
    return found

def reset_password(id):
    with open("register.txt",mode="r") as f:
        dict=eval(f.readline())
    reset=input("Enter new password : ")
    recheck=input("Re-enter the new password : ")
    if reset==recheck:
        del(recheck)#no use after the both the objects are same
        with open("register.txt",mode="w")as f:
            new_dict=dict[id]#phone no and password of the specified id
            new_key=tuple(new_dict)[0]#password as new key inorder to access nested dict
            phone_no=new_dict[new_key]#
            dict[id]={reset:phone_no}#password has been reset
            print("Password has been reset! Please try to login again.")
            f.write("{}".format(dict))

    else:
        print("Password mismatched!")
        print("\n")
        reset_password(id)

def check_otp():
    check=int(input("Enter OTP : "))
    with open("otp.txt",mode="r") as f:
        x=eval(f.readline())
    if check==x:pass
    else:
        print("Incorrect OTP!")
        sys.exit()

def check_password(id,password):
    """To check password of entered id"""
    with open("register.txt",mode="r") as f:
        flag=0#default value false
        dict=eval(f.readline())
        code=dict[id]#password and phone number
        code=tuple(code)#we get only password
       
        if code[0]==password:
            flag=1
        else:
            flag=0
    return flag

def interface():
    print("Press 1:To login id :")
    print("Press 2:To create new login id :")
    opt=int(input("Enter option : "))
    if opt==1:
        id=input("Enter id : ")   
        if check_id(id)==1:
            password=input("Enter password : ")
            if check_password(id,password)==1:
                print("Login Successful!")
                sys.exit()
            else:
                print("Wrong password!")
                print("Press 1 to generate OTP and reset password if forgotten")
                print("Press 2 to exit and re-login id ")
                choice=int(input("Enter your choice : "))
                if choice==1:
                    """generate otp and reset password!"""
                    OTP_generate(id)
                    check_otp()
                    reset_password(id)
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    interface()
        else:
            print("Wrong id!")
            sys.exit()
    elif opt==2:
        print("Create Your New Login ID :")
        print("##################################################################################################")
        with open("register.txt",mode="a+") as f:
            f.seek(0)
            x=len(f.readline())
            if x!=0:
                mode="a+"
                register(mode)#append mode if data already exist

            else:
                mode="w"
                register(mode)#creates a new file if it does not contain any datasys.exit()


#########################################################################################################################################
interface()
