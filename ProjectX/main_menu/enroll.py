import os
from main_menu import verify
import load
import time
def enroll_student():
	os.system("cls")
	print("\t 					o> Enrollment <o")
	print()
	new_student = input("o> Name\t:")
	student_sex = input("o> Sex\t:")
	student_grade = input("o> Grade:")
	student_date = input("o> Birthdate :")
	student_origin = input("o> Origin\t:")
	student_nationality = input("o> Nationality :")
	student_religion = input("o> Religion :")
	student_blood = input("o> Type of Blood :")
	student_telephone = input("o> Telephone Number :")
	student_father = input("o> Father's Name :")
	student_mother = input("o> Mother's Name :")
	student_address = input("o> Address\t:")
	student_weight = input("o> Weight\t:")
	student_height = input("o> Height\t:")
	print("Processing...")
	time.sleep(2)
	tampil = print("""
Is there any wrong data ?
[A]. Yes
[B]. No
	""")
	change = input("o> Your Answer :")
	if change.capitalize() == "A":
		wrong = input("o> Wrong Data\t:")
		new_value = input("o> New Value\t:")
		tampilan = print("""
Are you sure ?
[A]. Yes
[B]. No
			""")
		verify = input("o> Your Answer :")
		if verify.capitalize() == "A":
			print("Processing...")
			time.sleep(2)
			load.data[new_student] = {"Sex" : student_sex,
								  "Grade" : student_grade,
								  "Birthdate" : student_date,
								  "Origin" : student_origin,
								  "Nationality" : student_nationality,
								  "Religion" : student_religion,
								  "Blood Type" : student_blood,
								  "Telephone Number" : student_telephone,
								  "Father's Name" : student_father,
								  "Mother's Name" : student_mother,
								  "Address" : student_address,
								  "Weight" : student_weight,
								  "Height" : student_height}
			load.data[new_student][wrong] = new_value
			load.attendance["Student"] = new_student
			print("o> Processed")
			print("Thank you for joining Penguin Univeristy")
			print("Have a nice journey")
			print("""
If you have any problem with the data, you may contact any teacher.
				""")
			input("Press Enter to go back to Main Menu")
		elif verify == "B":
			print("Processing...")
			time.sleep(2)
			load.data[new_student] = {"Sex" : student_sex,
								  "Grade" : student_grade,
								  "Birthdate" : student_date,
								  "Origin" : student_origin,
								  "Nationality" : student_nationality,
								  "Religion" : student_religion,
								  "Blood Type" : student_blood,
								  "Telephone Number" : student_telephone,
								  "Father's Name" : student_father,
								  "Mother's Name" : student_mother,
								  "Address" : student_address,
								  "Weight" : student_weight,
								  "Height" : student_height}
			print("o> Processed")
			print("Thank you for joining Penguin Univeristy")
			print("Have a nice journey")
			print("""

If you have any problem with the data, you may contact any teacher.
				""")
			input("Press Enter to go back to Main Menu")
		else:
			print("Error! Register failed")
			input("Press Enter to go back to Main Menu")
	elif change == "B":
		print("Processing...")
		time.sleep(2)
		load.data[new_student] = {"Sex" : student_sex,
								  "Grade" : student_grade,
								  "Birthdate" : student_date,
								  "Origin" : student_origin,
								  "Nationality" : student_nationality,
								  "Religion" : student_religion,
								  "Blood Type" : student_blood,
								  "Telephone Number" : student_telephone,
								  "Father's Name" : student_father,
								  "Mother's Name" : student_mother,
								  "Address" : student_address,
								  "Weight" : student_weight,
								  "Height" : student_height}
		print("o> Processed")
		print("Thank you for joining Penguin Univeristy")
		print("Have a nice journey")
		print("""
If you have any problem with the data, you may contact any teacher.
			""")
		input("Press Enter to go back to Main Menu")
	else:
		print("Error! Register failed")
		input("Press Enter to go back to Main Menu")
