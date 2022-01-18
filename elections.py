import csv
def e_campaign():
    work_done =[]
    future_plan = []
    cname = input('Enter your name : ')
    pname = input('Enter your party name : ')
    
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
    with open('ecampaign','a') as ec:
        data = csv.writer(ec,dialect='excel')  
        data.writerow(['CANDIDATE','PARTY','SYMBOL','WROK DONE','FUTURE PLAN'])
        data.writerow([cname,pname,work_done,future_plan])

e_campaign()



def num_validader(n):
    while True:
        if len(n) == 10 and n.isnum():
            print('Approved.')
            break
        else:
            print('ERROR!! Try Again')
            n = input('Enter your mobile number ')

def username(u):
    un = 'E-'
    return un

def pas_check(p):
    while True:
        if len(p) == 6 and p.isalnum():
            print('Approved.')
            break
        else:
            print('ERROR!! Try Again')
            p = input('create password \n 1.It should be atleast 6 character.\n2.It should contain both number and alphabet.\n3.No special characters.')

def signup():
    name = input('Enter your first name ')
    lname = input('Enter your last name ')
    num = int(input('Enter your mobile number '))
    num_validader(num)
    id = input('Enter your voter id ')
    usern = username(id)
    pas = input('create password \n 1.It should be atleast 6 character.\n2.It should contain both number and alphabet.\n3.No special characters.')
    pas_check(pas)
    print('YOUR USERNAME : ',usern)
    with open('signup','a') as s:
        fh = csv.writer(s)
        fh.writerow('NAME','LAST NAME','MOBILE NUMBER','VOTER ID','USERNAME','PASSWORD')
        fh.writerow(name,lname,num,id,usern,pas)
    login()

def login():
    username = input('Enter username')
    password = input('Enter password')
    with open('signup','r') as l:
        fh = csv.reader(l)
        next(fh)
        i=0
        for line in fh:                                
            if username==line[-2]:                      #check whether username mentioned is correct or not.
                if password==line[-1]:
                    print('LOGED IN SUCCESSFULY')
                    break
                else:
                    print('ERROR!!')
                    password = input('Enter password')



