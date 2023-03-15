def credit_score(ac_balance,deposit,withdraw,loan_paid_per=0):
    """To calculate credit score for an individual"""
    c_score=0#credit_score

    def check_balance(ac_balance,c_score):
        """To check a/c balance limit"""
        if ac_balance>50000: #greater then Rs.50,0000
            c_score+=300
        elif ac_balance<=50000 and ac_balance>=35000:
            c_score+=200
        else:c_score+=100
        return c_score
    c_score=check_balance(ac_balance,c_score)
###################################################################################################################
    
    def transaction(deposit,withdraw,c_score):
        """To check no of transaction in the last 3 months"""
        if deposit+withdraw>=100:
            if deposit>=50 and withdraw>=50:
                c_score+=300
            else:pass
        else:pass
        return c_score
    
    c_score=transaction(deposit,withdraw,c_score)
##################################################################################################################
    def loan_eval(loan_paid_per,c_score):
        """To evaluate c_score base on repayment of loan"""
        if loan_paid_per>=90:
            c_score+=150
        elif loan_paid_per<90 and loan_paid_per>=70:
            c_score+=100
        elif loan_paid_per<70 and loan_paid_per>=50:
            c_score+=90
        elif loan_paid_per<50 and loan_paid_per>=20:
            c_score+=50
        elif loan_paid_per<20 and loan_paid_per>=1:
            c_score+=20
        else:pass
        return c_score
    c_score=loan_eval(loan_paid_per,c_score)
    return c_score
################################              main programme               ####################################
name=input("Enter your name : ")
ac_no=input("Enter your account no : ")
bank_name=input("Enter bank name : ")
ac_balance=int(input("Enter your current balance in account : "))
if ac_balance>0:
    print("Enter no of transaction in the last 3 months : ")
    deposit=int(input("No of deposit : "))
    withdraw=int(input("No of withdraw : "))
    loan_taken=input("Have u taken loan earlier? [y/n]: ")
    if loan_taken=="y" or loan_taken=="Y":
        loan_paid_per=int(input("How much loan have u paid ?[in %] : "))
    else:loan_paid_per=100#by default our credit score will be 150
    score=credit_score(ac_balance,deposit,withdraw,loan_paid_per)
    print("score",score)
    if score>700:
        print("Your credit score is {}\n\
            Congratulations! You are eligible to take the Loan".format(score))
    else:
        print("Your credit score is {}\n\
            Since your credit score is less then 700 hence, You are not eligible for loan !".format(score))
else:
    print("Since you dont have sufficient balance in your a/c, You are not eligible for withdrawl of loan !")
    exit()
