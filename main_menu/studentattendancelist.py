import os
import load
from main_menu import login
def attend():
	os.system("cls")
	print("					 o> Students Attendance List <o")
	print()
	print("<o-------------------------------------------------o>")
	for a in load.data:
		print("o> Name\t:", a)
		print("o> Grade:", load.data[a]["Grade"])
		print("o> Attendance :")
		for z, x in load.attendance["Student"][a].items():
			print(f"- {z} : {x}")
		print("<o-------------------------------------------------o>")
	input("Press Enter to go back to Main Menu")