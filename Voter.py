import csv
Dfile=open("store_.csv","a+")
csv.writer
def login_dets(): #basicinformation
    f_name=input("First Name-")
    s_name=input("Surname-")
    age=int(input("Age-"))
    age_check(age)
    gender=input("Male(M),Female(F),Other(O)-")
    dob=input("Date of Birth-(dd/mm/yyyy)")
    record=[f_name,s_name, str(age), gender, dob]
    stuwriter=csv.writer(Dfile)
    stuwriter.writerow(record)
    return
def age_check(q):#agecheck
    t=1
    if q<18:
        print("error,voting is only eligible for person who is 18 yrs old or above")
        quit()
        return
login_dets()
    
'''def d_o_b(): #datecheck
    m1=['01','03','05','08','10','12']
    m2=['04','06','07','09','11']
    m3=['02']
    m=login_dets(dob)[3:5]
    d=login_dets(dob)[0:2]
    y=login_dets(dob)[6:]
    if m in m1:
        if d=>31:
            print("error in dob")
    if m in m2:
        if d=>30:
            print("error in dob")
    if m in m3:
        if d=="29":
            if int(y)%4=!0:
                print("error in dob")
        elif d=>"29":
            print("error in dob")     
    return

def voter_info():
    id=input("Voter ID-")
    resd_=address()
    const_=input("Constituency from where you would like to vote-")

def address():
    while True:
    print("Provide the following details as per your address written in Aadhar Card")
    x=input("House/street/lane/sector no.-")
    y=input("Town-")
    z=input("District-")
    y=input("State")

def constituency_check():
    if address(z)=!voter_info(const_):
        print("error, address credentials do not match!")

def voting_boothreview():

def casting_vote():
    while True:
        print("Constituency-",z)
        #booth table display in form of list
        c_party=input("Party Name-")
        c_symbol=input("Symbol-")
        c_name.upper()
        c_party.upper()
        c_symbol.upper()
        vote=[c_name,c_party,c_symbol]
        if vote in '''








        