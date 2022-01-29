import csv
from candidate import *
from datetime import date
Dfile = open("store_.csv", "a+", newline='')
stuwriter = csv.writer(Dfile)

def login_dets():  # basic information of voter
    f_name = input("First Name-")
    f_name = f_name.upper()
    s_name = input("Surname-")
    s_name = s_name.upper()
    age = int(input("Age-"))
    age_=age_check(age)
    age=age_
    gender = input("Male(M),Female(F),Other(O)-")
    gender = gender.upper()
    while True:
        if gender not in ['M', 'F', 'O']:
         print("\t****Invalid information provided****")
         gender = input("Male(M),Female(F),Other(O)-")
         gender=gender.upper()
        else:
            break 
    dob = input("Date of Birth-(dd/mm/yyyy)-")
    d_o_b = age_dob(dob[6:], dob[3:5], dob[0:2])
    while True:
     if d_o_b != age:
            print("\t*****error,the age and dob do not match*****")
            dob = input("Date of Birth-(dd/mm/yyyy)-")
            d_o_b = age_dob(dob[6:], dob[3:5], dob[0:2])
     else:
         break           
    record_temp = [f_name, s_name, str(age), gender, dob]
    print('\n')
    print("\t*******Registration successful*******")
    print('\n')
    return record_temp


def age_check(q):  # agecheck
    while True:
        if q < 18:
            print("\t***error,voting is only eligible for person who is 18 yrs old or above***")
            q = int(input("Age-"))
        else:
            break    
    return q    
        

def age_dob(year, month, day):  # age and dob check
    today = date.today()
    age_ = today.year - int(year) - \
        ((today.month, today.day) < (int(month), int(day)))
    return age_


def voter_info(a):  # voting information
    id_ = input("Voter ID-")
    while True:
        if id_.isalnum() == False or len(id_) != 10:
            print('***ERROR TRY AGAIN***')
            id_ = input('Enter your voter id ')
        elif id_[0:3].isalpha() == False:
            print('***ERROR TRY AGAIN***')
            id_ = input('Enter your voter id ')
        elif id_[0:3].isupper()== False:
            print('***ERROR TRY AGAIN***')
            id_ = input('Enter your voter id ')
        elif id_[3:].isnumeric() == False:
            print('***ERROR TRY AGAIN***')
            id_ = input('Enter your voter id ')
        else:
            break    
    cc=voter_id_check(id_)
    cc=id_
    resd_, check_resd = address()
    const_ = input("Constituency from where you would like to vote-")
    const_ = const_.upper()
    r=constituency_check(check_resd, const_)
    const_=r
    const_ = const_.upper()
    ext = [id_, resd_, const_]
    final_rec = a+ext
    stuwriter.writerow(final_rec)
    Dfile.close()
    return const_


def address():  # address collector
    print('\n')
    print("\t***Please provide the following details as per your address written in Aadhar Card***")
    print("\n")
    x = input("House/street/appt. name/sector no.->")
    x = x.upper()
    area_list=['AZAD NAGAR','ANAND VIHAR','ANAND VIHAR COLONY','BABARPUR','BAHUBALI ENCLAVE','BALBIR NAGAR','DALLUPURA','DAYANAND VIHAR','DILSHAD COLONY','DILSHAD GARDEN','DURGA PURI','EAST VINOD NAGAR','GANDHI NAGAR','GANESH NAGAR','GAZIPUR','GEETA COLONY','GUJARAT VIHAR','HASANPUR VILLAGE','JAGATPURI','JHILMIL COLONY','JYOTI NAGAR(EAST)','JYOTI NAGAR(WEST)','KANTI NAGAR','KONDI','KALYAN PURI','KHUREJI KHAS','KRISHNA NAGAR','LAXMI NAGAR','MANDAOLI','MANDAWALI','MAYUR VIHAR','MAYUR VIHAR PHASE 1','MAYUR VIHAR PHASE 2','MAYUR VIHAR PHASE - 3','NEW ASHOK NAGAR','NEW GOBIND PURA','NEW KONDLI','NEW LAYALPUR COLONY','NIRMAN VIHAR','OLD ANARKALI','PANDAV NAGAR','PATPARGANJ','I.P.EXTENSION','PREET VIHAR','PUSPANJALI','SAINI ENCLAVE','SAVITA VIHAR','SHAHDARA','SHAKARPUR','SHRESHTHA VIHAR','SURAJMAL VIHAR','SURYA NIKETAN','SWASTHYA VIHAR','TAHIRPUR','TRILOKPURI','VASUNDHARA ENCLAVE','VISHWAS NAGAR','VIVEK VIHAR','VIGYAN VIHAR','WEST VINOD NAGAR','YAMUNA VIHAR','YOJANA VIHAR','MANSAROVAR PARK']
    print("The Major Localities in East Delhi are as follows: \n",)
    for i in area_list:
        print(i,end=" , ")
    print("\n")    
    print("On the basis of the above segment, please provide the following informations.")    
    y = input("Area/Locality->")
    y = y.upper()
    while True:
        if y not in area_list:
            print("\nThis portal is for the General Elections of EAST DELHI only.Any other area/locality provided is invalid as per the credentials.")
            print("Select any key to exit")
            print("Select @ to try again.")
            menu_no=input("Your corresponding choice-")
            if menu_no=="@":
                y=(input("Area/Locality->")).upper()
            else:
                quit()    
        else:
            break   
    z = input("District->")
    z = z.upper()
    while True:
        if z != 'EAST DELHI':
            print("\n***This portal is for the General Elections of EAST DELHI only. Any other district provided is invalid as per the credentials.***")
            print("Select any key to exit")
            print("Select # to try again.")
            menu=input("Your corresponding choice-")
            if menu=='#':
                z=(input("District-")).upper()
            else:
                quit()    
        else:
            break    
    w = input("State->")
    w = w.upper()
    while True:
        if w != 'NEW DELHI':
            print("\n***This portal is for the General Elections of EAST DELHI only. Any other state provided is invalid as per the credentials.***")
            print("Select any key to exit")
            print("Select % to try again.")
            menu=input("Your corresponding choice-")
            if menu=='%':
                w=(input("State-")).upper()
            else:
                quit()    
        else:
            break    
    address_ = x+','+y+','+z+','+w
    return address_, z

def constituency_check(o, n):  # constituency and dstrict check
    while True:
       if n!=o:
           print("\t*****error, address credentials do not match with the constituency from where you want to vote*****")
           n=input("Constituency from where you would like to vote-")
       else:
           break    
    return n

def casting_vote(c):  # casting vote
    print('\n')
    print("Constituency-", c)
    c_party = input("Party Name-")
    c_symbol = input("Symbol-")
    c_party = c_party.upper()
    c_symbol = c_symbol.upper()
    vote = [c_party, c_symbol]
    with open("campaign.csv",'r') as fh:
        data=csv.reader(fh)
        for party in data:                                                
                if party[2]==c_party:
                    listcheck=party
                    if listcheck[3] == c_symbol:
                        return vote
                    else:
                        while True:
                            print("\t\t***ERROR***\n INVALID SYMBOL")
                            c_symbol = (input("Symbol-")).upper()
                            if listcheck[3] == c_symbol:
                                vote = [c_party, c_symbol]
                                return vote              
        else:                
            print("Party does not exists")
            quit()


def voter_id_check(checkid):  # voter id repetion check
    check = [checkid]
    Efile=open("voter_id.csv", "r")
    ereader = csv.reader(Efile)
    for rec in ereader:
        if rec == check:
            print("\t\tERROR")
            print("******Voter ID already exists******")
            quit()
    Efile=open("voter_id.csv","a+",newline='')   
    stuwriter1 = csv.writer(Efile)
    stuwriter1.writerow([checkid])               

def result():       #polled result
    file = open("Results.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    vote_count = {}
    for row in csvreader:
        vote_count[row[0]] = vote_count.get(row[0],0) + 1
    print("THE POLLED RESULT: \n",vote_count)
    file.close()   
    v=list(vote_count.values())
    k=list(vote_count.keys())
    win=k[v.index(max(v))]
    P=0
    for i in v:
        P+=i
    print("\n")    
    print("TOTAL NUMBER OF VOTES:",P)
    print("\n")
    print("THE MAJORITY PARTY:",win,"\nVOTES:",max(v))

def voter_intro():      #intro for voting portal
    print("\n")
    print("WELCOME TO THE VOTING PORTAL")
    print("Voting is the expression of our commitment to ourselves, one another, this country, and this world")
    print('\n')
    print("Here you will be voting for the general elections")
    print("PLEASE COOPERATE AND PROVIDE THE FOLLOWING DETAILS CORRECTLY")
    print("\n")
    record = login_dets()
    constituency = voter_info(record)
    print("NOW WE WILL BE PROVIDING THE CANDIDATE TABLE FOR YOUR REVIEW")
    print('\n')
    table()
    result_list = casting_vote(constituency)
    print("\n")
    print("YOUR PRECIOUS VOTE IS SAFE WITH US")
    print("THANK YOU FOR USING OUR E-ELECTIONS PORTAL")
    print('\n')
    Rfile = open("Results.csv", "a", newline='')
    stuwriter2 = csv.writer(Rfile)
    stuwriter2.writerow(result_list)
    Rfile.close()

def intro():            #MAIN MENU 
    print("WELCOME TO OUR E-ELECTIONS PORTAL \n This portal is for the General Elections of EAST DELHI FOR MP.(Member of Parliament)")
    print()
    print("Select 1 if you are here to vote.")
    print("Select 2 if you are here to register as a candidate.")
    print("Select 3 if you want to login.(for candidates only)")
    print("Select 4 to view the polled result.")
    print("Select 5 to view the voting gender statistics.")
    print("Select 6 to view the candidate gender statistics.")
    print("Select any number to exit.")
    print()
    menu_number=int(input("Enter the number corresponding to your choice-->"))
    return menu_number

def voting_perc():          #REPORT
    print("M:MALE\nF:FEMALE\nO:OTHERS")
    file = open("store_.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    gender_ratio = {}
    for row in csvreader:
        gender_ratio[row[3]] = gender_ratio.get(row[3],0) + 1
    print(gender_ratio)
