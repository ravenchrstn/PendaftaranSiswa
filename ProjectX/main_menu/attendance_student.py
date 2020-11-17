import os
import load
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
	isi_daftarhadi = print(
			"""
Are you absent ?
[A]. Yes
[B]. No
			""")
	isi_daftarhadir = str(input("o> Your Answer :"))
	if isi_daftarhadir.capitalize() == "A":
		reason = input("o> Reason\t:")
		tanggalsekarang = tahun+"-"+bulan+"-"+tanggal
		load.attendance["Student"][login.name_user_student][tanggalsekarang] = f"Absent, {reason}"
		true = False
		print("Thank you")
	elif isi_daftarhadir.capitalize() == "B":
		tanggalsekarang = tahun+"-"+bulan+"-"+tanggal
		load.attendance["Student"][login.name_user_student][tanggalsekarang] = "Present"
		print("Thank you")
		true = False
	else:
		print("No command!")
		input("Press Enter to go back to Main Menu")			
#SAAT TAMBAH ADD KONTAK MASUK KE ATTENDANCE
	