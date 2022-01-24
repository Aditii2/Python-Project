#voter
 
from elections import *
from Voter import *
import csv

def create_CSVs():
    with open('campaign.csv','a+',newline='') as ec:
        data = csv.writer(ec)  

    with open('signup.csv','a+') as s:
        fh = csv.writer(s)
    
    Dfile = open("store_.csv", "a+", newline='')
    csv.writer
    stuwriter = csv.writer(Dfile)

create_CSVs()

menu = intro()

if menu == 1:
    voter_intro()
elif menu == 2:
    signup()
    e_campaign()
    table()
elif menu == 3:
    flagfin = login()
    if flagfin == True:
        table()
    else:
        intro()
elif menu == 4:
    result()



'''
for i in range (1,3):
    e_campaign()
#print(table())
'''

