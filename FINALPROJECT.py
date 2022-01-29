import csv
from candidate import *
from Voter import *


def create_CSVs():
    with open('campaign.csv', 'a+', newline='') as ec:
        data = csv.writer(ec)

    with open('signup.csv', 'a+') as s:
        fh = csv.writer(s)

    Dfile = open("store_.csv", "a+", newline='')
    stuwriter = csv.writer(Dfile)


create_CSVs()

menu = intro()

if menu == 1:
    voter_intro()
elif menu == 2:
    signup()
    e_campaign()
elif menu == 3:
    x = login()
    show_data(x)
elif menu == 4:
    result()
elif menu==5:
    voting_perc()
elif menu==6:
    candidate_perc()    
else:
    quit()
