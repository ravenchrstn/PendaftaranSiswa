import os
import load, save
import time
def enroll_student():
	os.system("cls")
	print("\t 					o> Enrollment <o")
	print()
	tru = True
	while tru:
		new_student = input("o> Name\t:")	
		if new_student.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		student_sex = input("o> Sex\t:")	
		if student_sex.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		try:
			student_grade = int(input("o> Grade:"))
			tru = False
		except ValueError:
			print("Please Input Number Only!")
	student_date = input("o> Birthdate :")
	tru = True
	while tru:
		student_origin = input("o> Origin:")
		if student_origin.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		student_nationality = input("o> Nationality :")
		if student_nationality.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		student_religion = input("o> Religion :")
		if student_religion.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		student_blood = input("o> Type of Blood :")
		if student_blood.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		try:
			student_telephone = int(input("o> Telephone Number :"))
			tru = False
		except ValueError:
			print("Please Input Number Only!")
	tru = True
	while tru:
		student_father = input("o> Father's Name :")
		if student_father.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	tru = True
	while tru:
		student_mother = input("o> Mother's Name :")
		if student_mother.isalpha() == True:
			tru = False
		else:
			print("Please Input Word Only")
	student_address = input("o> Address :")
	tru = True
	while tru:
		try:
			student_weight = int(input("o> Weight :"))
			tru = False
		except ValueError:
			print("Please Input Number Only!")
	tru = True
	while tru:
		try:
			student_height = int(input("o> Height :"))
			tru = False
		except ValueError:
			print("Please Input Number Only!")
	student_password = input("o> New Password :")
	print("Processing...")
	time.sleep(2)
	tampil = print("""
o> Is there any wrong data ?
[A]. Yes
[B]. No
[C]. Cancel
	""")
	change = str(input("o> Your Answer :"))
	if change.capitalize() == "A":
		wrong = str(input("o> Wrong Data\t:"))
		new_value = str(input("o> New Value\t:"))
		tampilan = print("""
o> Are you sure ?
[A]. Yes
[B]. No
			""")
		verify = str(input("o> Your Answer :"))
		if verify.capitalize() == "A":
			if wrong == "Name":
				new_student = new_value
			print("o> Processing...")
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
			load.datalogin["Student"][new_student] = student_password
			save.save_data_login()
			save.save_data_murid()
			save.save_data_hadir()
			print("o> Processed")
			print("Thank you for joining Penguin Univeristy")
			print("Have a nice journey")
			print("""
If you have any problem with the data, you may contact any teacher.
				""")
			input("Press Enter to go back to Main Menu")
		elif verify.capitalize() == "B":
			print("o> Processing...")
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
			load.attendance["Student"] = new_student
			load.datalogin["Student"][new_student] = student_password
			save.save_data_login()
			save.save_data_murid()
			save.save_data_hadir()
			print("o> Processed")
			print("Thank you for joining Penguin Univeristy")
			print("Have a nice journey")
			print("""

If you have any problem with the data, you may contact any teacher.
				""")
			input("Press Enter to go back to Main Menu")
		else:
			print("o> Error! Register failed")
			input("Press Enter to go back to Main Menu")
	elif change.capitalize() == "B":
		print("o> Processing...")
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
		load.attendance["Student"] = new_student
		load.datalogin["Student"][new_student] = student_password
		save.save_data_login()
		save.save_data_murid()
		save.save_data_hadir()
		print("o> Processed")
		print("Thank you for joining Penguin Univeristy")
		print("Have a nice journey")
		print("""
If you have any problem with the data, you may contact any teacher.
			""")
		input("Press Enter to go back to Main Menu")
	elif change.capitalize() == "C":
		print("o> Alright!")
		input("Press Enter to go back to Main Menu")
	else:
		print("o> Error! Register failed")
		input("Press Enter to go back to Main Menu")
