import os
import load
import time
from main_menu import verify
def update():
	os.system("cls")
	print("\t 					o> Update Data <o")
	nama_update = input("Name\t:")
	if nama_update in load.data:
		os.system("cls")
		ganti_apa = print("""
		Thing to Change.

		[A]. Name
		[B]. Sex
		[C]. Grade
		[D]. Birthdate
		[E]. Origin
		[F]. Nationality
		[G]. Religion
		[H]. Father's Name
		[I]. Mother's Name
		[J]. Blood Type
		[K]. Telephone Number
		[L]. Address
		[M]. Weight
		[N]. Height
			""")
		jawaban = input("		o> Your Answer\t:")
		print()
		if jawaban.capitalize() == "A":
			new_value = input("o> New Value\t:")
			print("Updating...")
			time.sleep(2)
			load.data[new_value] = load.data[nama_update]
			del load.data[nama_update]
			print("Data updated")
			input("Press Enter to go back to Main Menu")
		elif jawaban.capitalize() == "B" or jawaban.capitalize() == "C" or jawaban.capitalize() == "D" or jawaban.capitalize() == "E" or jawaban.capitalize() == "F" or jawaban.capitalize() == "G" or jawaban.capitalize() == "H" or jawaban.capitalize() == "I" or jawaban.capitalize() == "J" or jawaban.capitalize() == "K" or jawaban.capitalize() == "L" or jawaban.capitalize() == "M" or jawaban.capitalize() == "N":
			new_value = input("o> New Value\t:")
			verify.verify()
			B = "Sex"
			C = "Grade"
			D = "Birthdate"
			E = "Origin"
			F = "Nationality"
			G = "Religion"
			H = "Father's Name"
			I = "Mother's Name"
			J = "Blood Type"
			K = "Telephone Number"
			L = "Address"
			M = "Weight"
			N = "Height"
			if jawaban.capitalize() == "B":
				ubah = "Sex"
			elif jawaban.capitalize() == "C":
				ubah = "Grade"
			elif jawaban.capitalize() == "D":
				ubah = "Birthdate"
			elif jawaban.capitalize() == "E":
				ubah = "Origin"
			elif jawaban.capitalize() == "F":
				ubah = "Nationality"
			elif jawaban.capitalize() == "G":
				ubah = "Religion"
			elif jawaban.capitalize() == "H":
				ubah = "Father's Name"
			elif jawaban.capitalize() == "I":
				ubah = "Mother's Name"
			elif jawaban.capitalize() == "J":
				ubah = "Blood Type"
			elif jawaban.capitalize() == "K":
				ubah = "Telephone Number"
			elif jawaban.capitalize() == "L":
				ubah = "Address"
			elif jawaban.capitalize() == "M":
				ubah = "Weight"
			elif jawaban.capitalize() == "N":
				ubah = "Height"
			print("o> Updating...")
			load.data[nama_update][ubah] = new_value
			time.sleep(2)
			print("o> Data updated")
			input("Press Enter to go back to Main Menu")
		else:
			print("o> Command doesn't Found")
			input("Press Enter to go back to Main Menu")