import os
import load
def search():
	os.system("cls")
	print("\t 					o> Search Data <o")
	print()
	nama_cari = input("o> Name\t:")
	tempat = load.data
	for i in tempat:
		namaorang = i
	if nama_cari in load.data:
			os.system("cls")
			print(f"o> Name :", nama_cari)
			print(f"o> Sex :", tempat[nama_cari]["Sex"])
			print(f"o> Grade :", tempat[nama_cari]["Grade"])
			print(f"o> Birthdate :", tempat[nama_cari]["Birthdate"])
			print(f"o> Origin :", tempat[nama_cari]["Origin"])
			print(f"o> Nationality :", tempat[nama_cari]["Nationality"])
			print(f"o> Religion :", tempat[nama_cari]["Religion"])
			print(f"o> Father's Name :", tempat[nama_cari]["Father's Name"])
			print(f"o> Mother's Name :", tempat[nama_cari]["Mother's Name"])
			print(f"o> Blood Type :", tempat[nama_cari]["Blood Type"])
			print(f"o> Telephone Number :", tempat[nama_cari]["Telephone Number"])
			print(f"o> Address :", tempat[nama_cari]["Address"])
			print(f"o> Weight :", tempat[nama_cari]["Weight"])
			print(f"o> Height :", tempat[nama_cari]["Height"])
			input("Press Enter to go back to Main Menu")
	else:
		print("o> Student doesn't found")
		input("Press Enter to go back to Main Menu")