import load
import os
tempat = load.data

def kerja():
	os.system("cls")
	print("\t 					o> Student's Data <o")
	print()
	print("<o---------------------------------------------------------o>")
	for a in tempat:
		print(f"o> Name :", a)
		print(f"o> Sex :", tempat[a]["Sex"])
		print(f"o> Grade :", tempat[a]["Grade"])
		print(f"o> Birthdate :", tempat[a]["Birthdate"])
		print(f"o> Origin :", tempat[a]["Origin"])
		print(f"o> Nationality :", tempat[a]["Nationality"])
		print(f"o> Religion :", tempat[a]["Religion"])
		print(f"o> Father's Name :", tempat[a]["Father's Name"])
		print(f"o> Mother's Name :", tempat[a]["Mother's Name"])
		print(f"o> Blood Type :", tempat[a]["Blood Type"])
		print(f"o> Telephone Number :", tempat[a]["Telephone Number"])
		print(f"o> Address :", tempat[a]["Address"])
		print(f"o> Weight :", tempat[a]["Weight"]+" kg")
		print(f"o> Height :", tempat[a]["Height"]+" cm")
		print("<o---------------------------------------------------------o>")
	input("Press Enter to go back to Main Menu")
