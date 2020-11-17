import os
import load
import time
from main_menu import verify
def dropout():
	os.system("cls")
	print("\t 					o> Drop Out <o")
	print()
	nama_do = input("o> Name\t:")
	if nama_do in load.data:
		verify.verify()
		print("Deleting...")
		del load.data[nama_do]
		time.sleep(2)
		print("o> Data deleted")
		input("Press Enter to go back to Main Menu")
	else:
		print(f"{nama_do} is not found")
		input("Press Enter to go back to Main Menu")

