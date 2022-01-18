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
    with open('ecampaign','w') as ec:
        data = csv.writer(ec,dialect='excel')  
        data.writerow(['CANDIDATE','PARTY','SYMBOL','WROK DONE','FUTURE PLAN'])
        data.writerow([cname,pname,work_done,future_plan])
    print(cname,pname,work_done,future_plan)

e_campaign()
