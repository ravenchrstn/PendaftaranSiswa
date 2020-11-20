import os
import load, save
from datetime import date
from main_menu import login
global name_user_student
datenow = date.today()
tahun = datenow.year
bulan = datenow.month
tanggal = datenow.day
tahun, bulan, tanggal = str(tahun), str(bulan), str(tanggal)
def attendance():
	os.system("cls")
	true = True
	print("						o> Attendance <o")
	isi_daftarhadi = print(
			"""
o> Are you absent ?
[A]. Yes
[B]. No
			""")
	isi_daftarhadir = str(input("o> Your Answer :"))
	if isi_daftarhadir.capitalize() == "A":
		reason = str(input("o> Reason :"))
		tanggalsekarang = tahun+"-"+bulan+"-"+tanggal
		load.attendance["Teacher"][login.name_user_teacher][tanggalsekarang] = f"Absent, {reason}"
		save.save_data_hadir()
		true = False
		print("o> Thank you")
		input("Press Enter to go back to Main Menu")	
	elif isi_daftarhadir.capitalize() == "B":
		tanggalsekarang = tahun+"-"+bulan+"-"+tanggal
		load.attendance["Teacher"][login.name_user_teacher][tanggalsekarang] = "Present"
		save.save_data_hadir()
		true = False
		print("Thank you")
		input("Press Enter to go back to Main Menu")	
	else:
		print("No command found!")
		input("Press Enter to go back to Main Menu")	