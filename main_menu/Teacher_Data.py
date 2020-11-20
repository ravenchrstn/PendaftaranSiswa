import os
import load

def data():
	os.system("cls")
	print("\t 					o> Teacher's Data <o")
	print()
	print("<o---------------------------------------------------------o>")
	for a in load.data_guru:
		print(f"o> Name :", a)
		print(f"o> Subject :", load.data_guru[a]["Subject"])
		print("<o---------------------------------------------------------o>")
	input("Press Enter to go back to Main Menu")