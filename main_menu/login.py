import os
import load
from main_menu import menu_and_answer
def menu_login():
	os.system("cls")
	print("<o> What User ?")
	print("<A> Teacher")
	print("<B> Student")
	print("<C> Enroller")
	print(
"""
[ If you forget your password, try to ask any teacher for resetting your password ]
""")
def login_check():
	global user_login_answer
	global name_user_teacher, name_user_student
	menu_login()
	print()
	true = True
	while true:
		user_login_answer  = str(input("o> Your Answer :"))
		if user_login_answer.isnumeric() == True:
			print("Error! Letter Needed.")
		else:
			if len(user_login_answer) == 1:
				true = False
			else:
				print("Error! 1 Letter Needed.")
	if user_login_answer.capitalize() == "A":
		true = True
		while true:
			name_user_teacher = str(input("o> What is your name ? [Press 0 to stop]"))
			if name_user_teacher in load.datalogin["Teacher"]:
				while true:
					password_input = str(input("o> Enter the password :"))
					if password_input == load.datalogin["Teacher"][name_user_teacher]:
						true = False
					else:
						print("o> Password Wrong!")
			elif name_user_teacher == "0":
				return name_user_teacher
			else:
				print("o> User Unknown")
		menu_and_answer.tampilkan_menu_teacher_and_main_menu_answer()
	elif user_login_answer.upper() == "B":
		true = True
		while true:
			name_user_student = str(input("o> What is your name ? [ Press 0 to stop]"))
			if name_user_student in load.datalogin["Student"]:
				while true:
					password_input = str(input("o> Enter the password :"))
					if password_input == load.datalogin["Student"][name_user_student]:
						true = False
					else:
						print("o> Password Wrong!")
			elif name_user_student == "0":
				return name_user_student
			else:
				print("o> User Unknown")
		menu_and_answer.tampilkan_menu_student_and_main_menu_answer()
	elif user_login_answer.upper() == "C":
		menu_and_answer.tampilkan_menu_enroller_and_main_menu_answer()
	else:
		print("o> Command Unknown")
		login_check()
