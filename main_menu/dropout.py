import os
import load, save
import time
def dropout():
	os.system("cls")
	print("\t 					o> Drop Out <o")
	print()
	nama_do = str(input("o> Name\t:"))
	if nama_do in load.data:
		verify1 = print("""
o> Are you sure ?
[A]. Yes
[B]. No
""")
		verify = str(input("o> Your Answer :"))
		if verify.capitalize() == "A":
			print("o> Deleting...")
			del load.data[nama_do]
			del load.attendance["Student"][nama_do]
			time.sleep(2)
			save.save_data_murid()
			save.save_data_hadir()
			print("o> Data deleted")
			input("Press Enter to go back to Main Menu")
		elif verify.capitalize() == "B":
			print("o> Alright!")
			input("Press Enter to go back to Main Menu")
		else:
			print("o> Command Unknown")
			input("Press Enter to go back to Main Menu")
	else:
		print(f"o> {nama_do} does not found")
		input("Press Enter to go back to Main Menu")

