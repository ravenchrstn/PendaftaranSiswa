import load, save
import time
import os
from main_menu import login

def tempat():
	os.system("cls")
	print("							o> Change Password <o")
	print()
	new_pass = str(input("o> Your new password ?"))
	apakau3 = True
	while apakau3:
		verify1 = print("""
o> Are you sure ?
[A] Yes
[B] No
[C] Cancel
""")
		verify = str(input("o> Your Answer :"))
		if verify.capitalize() == "A":
			apakau3 = False
			print("o> Processing...")
			time.sleep(2)
			load.datalogin["Student"][login.name_user_student] = new_pass
			save.save_data_login()
			print("o> Processed")
			input("Press Enter to go back to login menu")
		elif verify.capitalize() == "B":
			newer_pass = str(input("o> Your new password ?"))
		elif verify.capitalize() == "C":
			apakau3 = False
			print()
			print("o> Alright!")
			input("Press Enter to go back to login menu")
		else:
			apakau3 = False
			print("o> Command Unknown!")
			input("Press Enter to go back to login menu")
