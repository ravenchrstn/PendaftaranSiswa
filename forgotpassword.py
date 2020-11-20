import load, save
import time
import os
from main_menu import verify
def tempat(siapa):
	apakau = True
	apakau2 = True
	while apakau:
		nama = input("Your name ? [Press 0 to stop]")
		if nama in load.datalogin[siapa]:
			apakau = False
			while apakau2:
				last_pass = input("Your last password ? [Press 0 to stop]")
				if last_pass == load.datalogin[siapa][nama]:
					apakau2 = False
					new_pass = input("Your new pass ?")
					apakau3 = True
					while apakau3:
						verify1 = print("""
Are you sure ?
[A] Yes
[B] No
""")
						verify = input("Your Answer :")
						if verify.capitalize() == "A":
							apakau3 = False
							print("Processing...")
							time.sleep(2)
							load.datalogin[siapa][nama] = new_pass
							save.save_data_login()
							print("Processed")
							input("Press Enter to go back to login menu")
						elif verify.capitalize() == "B":
							newer_pass = input("Your new pass ?")
				elif last_pass == "0":
					apakau2 = False
					print("Alright!")
					input("Press Enter to go back to login menu")
				else:
					print("Password Wrong! Try Again")
		elif nama == "0":
			apakau = False
			print("Alright!")
			input("Press Enter to go back to login menu")
		else:
			apakau = False
			print("User unknown")
			input("Press Enter to go back to login menu")

def forgot():
	os.system("cls")
	siapa1 = print("""
What user ?
[A]. Teacher
[B]. Student
""")
	siapa = input("Your Answer :")
	if siapa.capitalize() == "A":
		tempat(siapa="Teacher")
	elif siapa.capitalize() == "B":
		tempat(siapa="Student")
