def login_dets(): #basicinformation
    f_name=input("First Name-")
    s_name=input("Surname-")
    age=int(input("Age-"))
    gender=input("Male(M),Female(F),Other(O)-")
    dob=input("Date of Birth-(dd/mm/yyyy)")


def age_check(): #agecheck
    if login_dets(age)<18:
        print("error in age")
        return
    
def d_o_b(): #datecheck
    m1=['01','03','05','08','10','12']
    m2=['04','06','07','09','11']
    m2=['02']
    m=login_dets(dob)[3:5]
    d=login_dets(dob)[0:2]
    y=login_dets(dob)[6:]
    if x in m1:
        
        

    
    
            
