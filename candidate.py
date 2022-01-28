import csv
import pwinput


def e_campaign():   #CANDIDATE E CAMPAIGNING
    print("\nWELCOME TO E-CAMPAIGN PORTAL\n") 
    print('Strong people stand up for themselves, but stronger people stand up for others.\n ')
    work_done =[]
    future_plan = []
    cname = (input('Enter your name : ')).upper()
    sname=(input("Enter your surname : ")).upper()
    pname = (input('Enter your party name : ')).upper()
    psym = (input('Enter your party symbol : ')).upper()
    
    while True:
        resp = input('do you want to enter previous work done? (y/n) : ')
        if resp.lower() == 'y':
            w_d = input('Enter your previous work done when elected : ')
            work_done.append(w_d)
        else:
            break
    f_p = input('Enter your Current Agenda : ')
    future_plan.append(f_p)
    while True:
        resp = input('do you want to enter more? (y/n) : ')
        if resp.lower() == 'y':
            f_p = input('Enter your Current Agenda : ')
            future_plan.append(f_p)
        elif resp.lower() == 'n':
            break
    with open('campaign.csv','a',newline='') as fh:
        dat = csv.writer(fh)  
        dat.writerow([cname,sname,pname,psym,work_done,future_plan])


def num_validader(n):       #CHECK ENTERED MOBILE NUMBER
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
            print('\n\t\t******Approved.*******\n')
            break
        else:
            print('\n\t\t*****ERROR!! Try Again******\n')
            p = input('create password \n 1.It should be atleast 6 character.\n2.It should contain both number and alphabet.\n3.No special characters.')


def voterid_check(v):      # CHECK FORMAT OF VOTER ID                             
    while True:
        x=v
        if v.isalnum() == False or len(v) != 10:
            print('***ERROR TRY AGAIN***')
            v = input('Enter your voter id ')
        elif v[0:3].isalpha() == False:
            print('***ERROR TRY AGAIN***')
            v = input('Enter your voter id ')
        elif v[0:3].isupper()== False:
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
    name = (input('Enter your first name : ')).upper()
    lname = (input('Enter your last name : ')).upper()
    gender = (input("Male(M),Female(F),Other(O)- : ")).upper()
    while True:
        if gender not in ['M', 'F', 'O']:
         print("\t***Invalid information provided***")
         gender = (input("Male(M),Female(F),Other(O)- : ")).upper()
        else:
            break 
    num = int(input('Enter your mobile number : '))
    num_validader(num)
    id = input('Enter your voter id : ')
    voter_id_check(id)
    usern = username(id)
    password = pwinput.pwinput(prompt='create password \n\n 1.It should be atleast 6 character.\n 2.It should contain both number and alphabet.\n 3.No special characters.\n\n Enter: ', mask='*') # Change the prompt.
    pas_check(password)
    print('\nYOUR USERNAME : ',usern)
    with open('signup.csv','a',newline='\n') as s:
        fh = csv.writer(s)
        fh.writerow([name,lname,gender,num,id,usern,password])
    print('SUCCESSFULY CREATED AN ACCOUNT.\n\nLOGIN\n')
    login()


def login():                    #CANDIDATE LOGIN 
    username = input('Enter username : ')
    with open('signup.csv','r', newline ='\n') as l:
        fh = csv.reader(l)
        next(fh)
        for line in fh:                                                
            if line[-2]==username:
                listcheck=line
                password = pwinput.pwinput(prompt='Enter Password : ', mask='*') # Change the prompt.
                if listcheck[-1] == password:
                    print('\n***SUCCESSFULLY LOGGED IN***\n')
                    return username
                else:
                    while True:
                        print("\t\t***ERROR***")
                        print("\t\t wrong password\n\t\tTRY AGAIN")
                        password = pwinput.pwinput(prompt='Enter Password : ', mask='*') # Change the prompt.
                        if listcheck[-1] == password:
                            print('\n***SUCCESSFULLY LOGGED IN***\n')
                            return username            
        else:                
            print("User does not exists")
            quit() 


def voter_id_check(checkid):  # VOTER ID REPETETION AND EXISTENCE CHECK
    check = [checkid]
    Efile=open("voterid_can.csv", "r")
    ereader = csv.reader(Efile)
    for rec in ereader:
        if rec == check:
            print("\t\tERROR")
            print("***Voter ID already exists***")
            quit()
    Efile=open("voterid_can.csv","a+",newline='')   
    stuwriter1 = csv.writer(Efile)
    stuwriter1.writerow([checkid])


from prettytable import PrettyTable     
from prettytable import from_csv

def table():                        #TABULAR PRESENTATION OF CAMPAIGNING
    f = open('campaign.csv','r')
    x = from_csv(f)
    print(x)


def candidate_perc():           #REPORT
    print("M:MALE\nF:FEMALE\nO:OTHERS")
    file = open("signup.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    gender_ratio = {}
    for row in csvreader:
        gender_ratio[row[2]] = gender_ratio.get(row[2],0) + 1
    print(gender_ratio)
    file.close()


def show_data(a):       # CANDIDATE CAMPAIGNING DATA AFTER LOGIN
    name = ''
    lname = ''
    with open('signup.csv','r') as fh:
        data = csv.reader(fh)
        next(data)
        for info in data:
            if info[-2] == a:
                name = info[0]
                lname = info[1]
                with open('campaign.csv','r') as dh:
                    d2 = csv.reader(dh)
                    for l in d2:
                        if l[0] == name and l[1] == lname:
                                print('NAME\t                  : ',l[0])
                                print('SURNAME\t                  : ',l[1])
                                print('PARTY\t                  : ',l[2])
                                print('SYMBOL\t                  : ',l[3])
                                print('PREVIOUS WORK DONE\t  : ',l[4])
                                print('CURRENT AGENDA\t          : ',l[0])
                                    