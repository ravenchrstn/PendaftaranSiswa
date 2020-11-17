import load
import os
tempat = load.data

def kerja():
	os.system("cls")
	print("\t 					o> Student's Data <o")
	print()
	print("<o---------------------------------------------------------o>")
	for a in tempat:
		print(f"Name :", a)
		print(f"Sex :", tempat[a]["Sex"])
		print(f"Grade :", tempat[a]["Grade"])
		print(f"Birthdate :", tempat[a]["Birthdate"])
		print(f"Origin :", tempat[a]["Origin"])
		print(f"Nationality :", tempat[a]["Nationality"])
		print(f"Religion :", tempat[a]["Religion"])
		print(f"Father's Name :", tempat[a]["Father's Name"])
		print(f"Mother's Name :", tempat[a]["Mother's Name"])
		print(f"Blood Type :", tempat[a]["Blood Type"])
		print(f"Telephone Number :", tempat[a]["Telephone Number"])
		print(f"Address :", tempat[a]["Address"])
		print(f"Weight :", tempat[a]["Weight"])
		print(f"Height :", tempat[a]["Height"])
		print("<o-----------------------------------------------------o>")
	input("Press Enter to go back to Main Menu")
