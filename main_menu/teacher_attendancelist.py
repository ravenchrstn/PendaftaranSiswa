import os
import load
def attend():
	os.system("cls")
	print("					 o> Teachers Attendance List <o")
	print()
	print("<o-------------------------------------------------o>")
	for a in load.data_guru:
		print("o> Name\t:", a)
		print("o> Attendance :")
		for z, x in load.attendance["Teacher"][a].items():
			print(f"  - {z} : {x}")
		print("<o-------------------------------------------------o>")
	input("Press Enter to go back to Main Menu")