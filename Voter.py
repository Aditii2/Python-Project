import csv
from datetime import date
Dfile = open("store_.csv", "a+")
csv.writer
stuwriter = csv.writer(Dfile)


def login_dets():  # basicinformation
    f_name = input("First Name-")
    f_name = f_name.upper()
    s_name = input("Surname-")
    s_name = s_name.upper()
    age = int(input("Age-"))
    age_check(age)
    gender = input("Male(M),Female(F),Other(O)-")
    gender = gender.upper()
    if gender not in ['M', 'F', 'O']:
        print("!!!!Invalid information provided!!!!")
        quit()
    dob = input("Date of Birth-(dd/mm/yyyy)-")
    t = dob_check(dob)
    d_o_b = age_dob(dob[6:], dob[3:5], dob[0:2])
    if d_o_b != age:
        print("!!!!!error,the age and dob do not match!!!!!")
        quit()
    record_temp = [f_name, s_name, str(age), gender, dob]
    print('\n')
    print("!!!!!!!Registration successful!!!!!!!")
    print('\n')
    return record_temp


def age_check(q):  # agecheck
    if q < 18:
        print("error,voting is only eligible for person who is 18 yrs old or above")
        quit()
        return


def age_dob(year, month, day):  # age and dob check
    today = date.today()
    age_ = today.year - int(year) - \
        ((today.month, today.day) < (int(month), int(day)))
    return age_


def dob_check(p):  # datecheck
    m1 = ['01', '03', '05', '08', '10', '12']
    m2 = ['04', '06', '07', '09', '11']
    m3 = ['02']
    m = p[3:5]
    d = p[0:2]
    y = p[6:]
    if m in m1:
        if d > "31":
            print("error in dob")
            print("Try Again")
            quit()
    if m in m2:
        if d > "30":
            print("error in dob")
            print("Try Again")
            quit()
    if m in m3:
        if d == "29":
            if int(y) % 4 != 0:
                print("error in dob")
                print("Try Again")
                quit()
        elif d > "29":
            print("error in dob")
            print("Try Again")
            quit()
    return


def voter_info(a):  # voting information
    id_ = input("Voter ID-")
    if id_.isalnum == False:
        print('!!!!Invalid voter ID, voter ID should be alphanumeric. PLEASE TRY AGAIN!!!!')
        quit()
    if len(id_) != 10:
        print('!!!!Ivalid Voter ID, Voter ID is a combination of 10 alphanumeric characters. PLEASE TRY AGAIN!!!!')
        quit()
    if id_[0:3].isalpha == False:
        print('!!!!Invalid Voter ID!!!!')
        quit()
    if id_[0:3].isupper() == False:
        print('!!!!Invalid Voter ID!!!!')
        quit()
    voter_id_check(id_)
    resd_, check_resd = address()
    const_ = input("Constituency from where you would like to vote-")
    const_ = const_.upper()
    constituency_check(check_resd, const_)
    ext = [id_, resd_, const_]
    final_rec = a+ext
    stuwriter.writerow(final_rec)
    Dfile.close()
    return const_


def address():  # address collector
    print("***Please provide the following details as per your address written in Aadhar Card***")
    x = input("House/street/lane/appt. name/sector no.->")
    x = x.upper()
    y = input("Town->")
    y = y.upper()
    z = input("District->")
    z = z.upper()
    w = input("State->")
    w = w.upper()
    address_ = x+','+y+','+z+','+w
    return address_, z


def constituency_check(o, n):  # constituency and dstrict check
    if n != o:
        print("*****error, address credentials do not match with the constituency from where you want to vote*****")
        quit()
    return


def casting_vote(c):  # casting vote
    print("Constituency-", c)
    c_party = input("Party Name-")
    c_symbol = input("Symbol-")
    c_party = c_party.upper()
    c_symbol = c_symbol.upper()
    vote = [c_party, c_symbol]
    print(vote)
    return


def voter_id_check(checkid):  # voter id repetion check
    check = [checkid]
    with open("voter_id.csv", "r") as Efile:
        ereader = csv.reader(Efile)
        for rec in ereader:
            if rec == check:
                print("ERROR")
                print("!!!!!!Voter ID already exists!!!!!!")
                quit()
    Efile = open("voter_id.csv", "a+")
    stuwriter1 = csv.writer(Efile)
    stuwriter1.writerow([checkid])
    Efile.close()
    return


print("\n")
print("WELCOME TO THE VOTER PORTAL")
print("Voting is the expression of our commitment to ourselves, one another, this country, and this world")
print('\n')
print("Here you will be voting for the general elections")
print("PLEASE COOPERATE AND PROVIDE THE FOLLOWING DETAILS CORRECTLY")
print("\n")
record = login_dets()
constituency = voter_info(record)
print("NOW WE WILL BE PROVIDING THE CANDIDATE TABLE FOR YOUR REVIEW")
casting_vote(constituency)
print("\n")
print("YOUR PRECIOUS VOTE IS SAFE WITH US")
print("THANK YOU FOR USING OUR E-ELECTIONS PORTAL")
print('\n')
