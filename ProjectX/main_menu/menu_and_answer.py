import os
from datetime import datetime
from main_menu import students_data, enroll, dropout, update_data, searching, aboutapp, aboutschool, attendance_student, pricelist, studentattendancelist

tanggal_sekarang = datetime.today().strftime("%Y-%m-%d")
title = "Penguin Univeristy"
title_middle = title.title()
main_menu_teacher = f"""
						o> {title_middle} <o
													{tanggal_sekarang}
   Main Menu :

   <A> Students' Data
   <B> Drop Out
   <C> Update Student's Data
   <D> Searching for Specific Student's Data
   <E> About this app
   <I> About school
   <Q> Quit
"""

main_menu_student = f"""
						o> {title_middle} <o
													{tanggal_sekarang}
   Main Manu : 

   <A> Students' Data
   <B> Attendance
   <C> Attendance List
   <D> Searching for Specific Student's Data
   <E> About this app
   <I> About school
   <Q> Quit
"""

main_menu_enroller = f"""
						o> {title_middle} <o
													{tanggal_sekarang}
   Main Menu :

   <A> Enroll
   <B> Price List
   <C> Students' Data
   <D> Searching for Specific Student's Data
   <I> About this school
   <Q> Quit
"""

def tampilkan_menu_teacher_and_main_menu_answer():
   global teacher_answer
   while True:
      os.system("cls")
      print(main_menu_teacher)
      teacher_answer = input("o> Your Answer :")
      if teacher_answer.capitalize()  == "A":
         students_data.kerja()
      elif teacher_answer.capitalize() == "B":
         dropout.dropout()
      elif teacher_answer.capitalize() == "C":
         update_data.update()
      elif teacher_answer.capitalize() == "D":
         searching.search()
      elif teacher_answer.capitalize() == "E":
         aboutapp.aboutapp()
      elif teacher_answer.capitalize() == "I":
         aboutschool.aboutschool()
      elif teacher_answer.capitalize() == "Q":
         break

def tampilkan_menu_student_and_main_menu_answer():
   global student_answer
   while True:
      os.system("cls")
      print(main_menu_student)
      student_answer = input("o> Your Answer :")
      if student_answer.capitalize()  == "A":
         students_data.kerja()
      elif student_answer.capitalize() == "B":
         attendance_student.attendance()
      elif student_answer.capitalize() == "C":
         studentattendancelist.attend()
      elif student_answer.capitalize() == "D":
         searching.search()
      elif student_answer.capitalize() == "E":
         aboutapp.aboutapp()
      elif student_answer.capitalize() == "I":
         aboutschool.aboutschool()
      elif student_answer.capitalize() == "Q":
         break

def tampilkan_menu_enroller_and_main_menu_answer():
   global enroller_answer
   while True:
      os.system("cls")
      print(main_menu_enroller)
      enroller_answer = input("o> Your Answer :")
      if enroller_answer.capitalize()  == "A":
         enroll.enroll_student()
      elif enroller_answer.capitalize() == "B":
         pricelist.enroll_student()
      elif enroller_answer.capitalize() == "C":
         students_data.kerja()
      elif enroller_answer.capitalize() == "D":
         searching.search()
      elif enroller_answer.capitalize() == "I":
         aboutschool.aboutschool()
      elif enroller_answer.capitalize() == "Q":
         break

