
#voter
 
from elections import e_campaign, table
import csv


def create_CSVs():
    with open('campaign.csv','w',newline='') as ec:
        data = csv.writer(ec)  
        data.writerow(['CANDIDATE','PARTY','SYMBOL','WORK DONE','FUTURE PLAN'])

    with open('signup.csv','w') as s:
        fh = csv.writer(s)
        fh.writerow(['NAME','LAST NAME','MOBILE NUMBER','VOTER ID','USERNAME','PASSWORD'])
    
    



create_CSVs()
for i in range (1,3):
    e_campaign()
#print(table())

