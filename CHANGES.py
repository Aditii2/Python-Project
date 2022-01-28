#add message for campaign -----------------
#username and signup check---------------
#add asterisk while writing the password--------------
#upper case names ----------------
#Female voting percentage------------
#Male voting percentage----------
#Others voting percentage----------
#Add gender column to signup ---------------
#Female candidate percentage-----------
#Male candidate percentage-------------
#Others candidate percentage------------
#Add majority party in result----------------
#no logic in flag --------------
#Constituency east delhi ----------
#elections member of parliament mp -----------
#upper check for voter id----------------
#east delhi constituency check edit----------
#area edited ----------
#add voterid check candidate------------
#constituency east de check---------
#while voting party symbol check----------------
#add list of major localities of east delhi with area check--------------
#remove area and locality---------------
#show data of candidate only while logging in---------------------



constituency_list=["GANDHI NAGAR","KONDLI","PATPARGANJ","KRISHNA NAGAR","TRILOKPURI","LAXMI NAGAR","VISHWAS NAGAR","OKHLA"]


x="Azad Nagar Anand Vihar Colony Babarpur Bahubali Enclave Balbir Nagar Dallupura Dayanand Vihar Dilshad colony Dilshad Garden Durga Puri East Vinod Nagar Gandhi Nagar Ganesh Nagar Gazipur Geeta Colony Gujarat Vihar Hasanpur Village Jagatpuri Jhilmil colony Jyoti Nagar(east) Jyoti Nagar(west) Kanti nagar Kalyan Puri Khureji khas Krishna Nagar Laxmi Nagar (Delhi) Mandaoli Mandawali Mayur Vihar Mayur Vihar Phase - 3 New Ashok Nagar New Gobind Pura New Kondli New Layalpur Colony Nirman Vihar Old anarkali Pandav Nagar Patparganj (I.P.Extension) Preet Vihar Puspanjali Saini Enclave Savita Vihar Shahdara Shakarpur Shreshtha vihar Surajmal Vihar Surya Niketan Swasthya Vihar Tahirpur Trilokpuri Vasundhara Enclave Vishwas Nagar Vivek Vihar Vigyan Vihar West Vinod Nagar Yamuna Vihar Yojana Vihar Mansarovar park".upper()

area_list=['AZAD NAGAR','ANAND VIHAR','ANAND VIHAR COLONY','BABARPUR','BAHUBALI ENCLAVE','BALBIR NAGAR','DALLUPURA','DAYANAND VIHAR','DILSHAD COLONY','DILSHAD GARDEN','DURGA PURI','EAST VINOD NAGAR','GANDHI NAGAR','GANESH NAGAR','GAZIPUR','GEETA COLONY','GUJARAT VIHAR','HASANPUR VILLAGE','JAGATPURI','JHILMIL COLONY','JYOTI NAGAR(EAST)','JYOTI NAGAR(WEST)','KANTI NAGAR','KONDI','KALYAN PURI','KHUREJI KHAS','KRISHNA NAGAR','LAXMI NAGAR','MANDAOLI','MANDAWALI','MAYUR VIHAR','MAYUR VIHAR PHASE 1','MAYUR VIHAR PHASE 2','MAYUR VIHAR PHASE - 3','NEW ASHOK NAGAR','NEW GOBIND PURA','NEW KONDLI','NEW LAYALPUR COLONY','NIRMAN VIHAR','OLD ANARKALI','PANDAV NAGAR','PATPARGANJ','I.P.EXTENSION','PREET VIHAR','PUSPANJALI','SAINI ENCLAVE','SAVITA VIHAR','SHAHDARA','SHAKARPUR','SHRESHTHA VIHAR','SURAJMAL VIHAR','SURYA NIKETAN','SWASTHYA VIHAR','TAHIRPUR','TRILOKPURI','VASUNDHARA ENCLAVE','VISHWAS NAGAR','VIVEK VIHAR','VIGYAN VIHAR','WEST VINOD NAGAR','YAMUNA VIHAR','YOJANA VIHAR','MANSAROVAR PARK']

'''
def edit_campaign(a):
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
                            print(l)
                            resp = input('Enter $ to edit your future agenda \n Select any number to exit\nEnter : ')
                            if resp == '$':
                                f_p = input('Enter your current agenda : ')
                                with open('campaign.csv','a') as s :
                                    w = csv.writer(s)
                                    l+= [f_p]
                                    print(l)
                                while True:
                                    resp = input('do you want to enter more? (y/n)')
                                    if resp.lower() == 'y':
                                        f_p = input('Enter your current agenda : ')
                                        l += [f_p]
                                        print(l)
                                    elif resp.lower() == 'n':
                                        break
                            else:
                                quit()
 '''   