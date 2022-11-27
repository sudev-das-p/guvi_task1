import re
import csv
email_regex = re.compile('\w+([A-Za-z0-9\.]+)*@[A-za-z]+(\.[A-za-z]+)')
pword_regex = re.compile('^(?=.*[A-Z][a-z])(?=.*\d)(?=.*[\W\D])[A-Za-z\d\W\D]{8,}$')

def emailValidity(email):
	if re.fullmatch(email_regex,email):
		return True
	else:
		return False
def pwordValidity(pword):
	if re.fullmatch(pword_regex,pword):
		return True
	else:
		return False
def register():
	print('\nRegister new user\n')
	email = input("Enter mail id : ")
	if emailValidity(email):
		pword = input("Enter password : ")
		if pwordValidity(pword):
			write_file(email,pword)
			print('\nUser Registered SUccessfully\n')
		else:
			print("\nInvalid Password\n")
	else:
		print("\nInvalid Username\n")
def login():
	email = input("\nEnter mail id : ")
	if emailValidity(email):
		pword = input("\nEnter password\n")
		if pwordValidity(pword):
			if search_file(email,pword):
				print("\nUser logged in successfully\n")
			else:
				print("\nUser not found\n")
				register()
		else:
			print("\n Enter valid password\n")
	else:
		print("\nEnter valid mail id\n")
def forgetPassword():
	email = input("\nEnter mail id : ")
	if emailValidity(email):
		if search_pword(email):
			print("\n User logged in successfully")
		else:
			print("\nUser not found")
			register()
	else:
		print("\nInvalid mail id")
def write_file(email,password):
	userfile = open('users.csv','w',newline = '')
	writer = csv.writer(userfile)
	writer.writerow([email,password])
def search_file(email,password):
	userfile = open('users.csv','r',newline = '')
	reader = csv.reader(userfile)
	for r in reader:
		if email==r[0] and password==r[1]:
			return True
	return False
def search_pword(email):
	userfile = open('users.csv','r',newline = '')
	reader = csv.reader(userfile)
	for r in reader:
		if email==r[0]:
			return True
	return False


if __name__ == "__main__":
	while True:
            print(''' \nPlease select an option \n
                1. Register
                2. Login
                3. Forget Password
                ''')
            option = int(input())
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                forgetPassword()
            else:
                print("Invalid Option")
   

   


