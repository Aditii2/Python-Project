import csv

def e_campaign():   #FUNCTION FOR CANDIDATE FOR E CAMPAIGNING 
    work_done =[]
    future_plan = []
    cname = input('Enter your name : ')
    pname = input('Enter your party name : ')
    psym = input('Enter your party symbol : ')
    
    while True:
        resp = input('do you want to enter previous work done? (y/n)')
        if resp.lower() == 'y':
            w_d = input('Enter your previous work done when elected : ')
            work_done.append(w_d)
        else:
            break
    f_p = input('Enter your current agenda : ')
    future_plan.append(f_p)
    while True:
        resp = input('do you want to enter more? (y/n)')
        if resp.lower() == 'y':
            f_p = input('Enter your current agenda : ')
            future_plan.append(f_p)
        elif resp.lower() == 'n':
            break
    with open('campaign.csv','a',newline='') as fh:
        dat = csv.writer(fh)  
        dat.writerow([cname,pname,psym,work_done,future_plan])

def num_validader(n):       #CHECK ON ENTERED MOBILE NUMBER
    while True:
        if len(str(n)) == 10 and str(n).isnumeric():
            print('\n\t\t******Approved.*******\n')
            break
        else:
            print('\n\t\t*****ERROR!! Try Again******\n')
            n = input('Enter your mobile number ')

def username(u):        #USERNAME GENERATOR FOR CANDIDATE
    un = 'E-ELEC-'+u
    return un

def pas_check(p):       #CHECK PASSWORD 
    while True:
        if len(p) >= 6 and p.isalnum():
            print('\n\t\t******Approved.*******')

            break
        else:
            print('\n\t\t*****ERROR!! Try Again******')
            p = input('create password \n 1.It should be atleast 6 character.\n2.It should contain both number and alphabet.\n3.No special characters.')


'''
def voter_id_check(checkid):  # voter id repetion check
    check = [checkid]
    with open("voter_id_cand.csv", "r") as Efile:
        ereader = csv.reader(Efile)
        for rec in ereader:
            if rec == check:                #ERROR
                print("ERROR")
                print("!!!!!!Voter ID already exists!!!!!!")
                quit()
    Efile = open("voter_id.csv", "a+")
    stuwriter1 = csv.writer(Efile)
    stuwriter1.writerow([checkid])
'''

def voterid_check(v):                                   ####### CHECK #######
    while True:
        x=v
        if v.isalnum() == False or len(v) != 10:
            print('***ERROR TRY AGAIN***')
            v = input('Enter your voter id ')
        elif v[0:3].isalpha() == False:
            print('***ERROR TRY AGAIN***')
            v = input('Enter your voter id ')
        elif v[3:].isnumeric() == False:
            print('***ERROR TRY AGAIN***')
            v = input('Enter your voter id ')
        else:
            with open('voterid_can.csv','a') as store:
                l = csv.writer(store)
                l.writerow(v)
            print('Voter id approved.')
            break


def signup():       #SIGNUP FOR CANDIDATE
    name = input('Enter your first name ')
    lname = input('Enter your last name ')
    num = int(input('Enter your mobile number '))
    num_validader(num)
    id = input('Enter your voter id ')
    voterid_check(id)
    usern = username(id)
    pas = input('create password \n\n 1.It should be atleast 6 character.\n 2.It should contain both number and alphabet.\n 3.No special characters.\n\n Enter : ')
    pas_check(pas)
    print('\nYOUR USERNAME : ',usern)
    with open('signup.csv','a',newline='\n') as s:
        fh = csv.writer(s)
        fh.writerow([name,lname,num,id,usern,pas])
    print('SUCCESSFULY CREATED AN ACCOUNT.\n\nLOGIN\n')
    login()


def login():
    username = input('Enter username : ')
    password = input('Enter password : ')
    with open('signup.csv','r', newline ='\n') as l:
        fh = csv.reader(l)
        next(fh)
        '''for row in fh:
            if username == row[-2] and password== row[-1]:
              print('\n***APPROVED***')
            else:
                print('\n***INCORRECT CREDENTIALS TRY AGAIN***\n')
                username = input('Enter username : ')
                password = input('Enter password : ')
'''
        for line in fh:                                
            if line[-2] != username:                      #check whether username mentioned is correct or not.
                continue
            else:
                if line[-1] == password:
                    print('\n***SUCCESSFULLY LOGGED IN***\n')
                    break
                else:
                    password = input('Enter password : ')
                    
login()

        

from prettytable import PrettyTable                     # NEW MODULE
from prettytable import from_csv

def table():
    #file_path = 'C:\Users\I539833\Desktop\Aditi\Python Project'
    f = open('campaign.csv','r')
    x = from_csv(f)
    return x


# DEFINE LOGIN FUNCTION
