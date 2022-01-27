import pwinput
user_name = input('Enter User Name: ')
password = pwinput.pwinput(prompt='Enter Password: ', mask='*')

print(password)