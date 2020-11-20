import os
from datetime import datetime
from main_menu import Teacher_Data, attendance_teacher, teacher_attendancelist, forgotpasswordteacher, forgotpasswordstudent, students_data, enroll, dropout, update_data, searching, aboutapp, aboutschool, attendance_student, pricelist, studentattendancelist


tanggal_sekarang = datetime.today().strftime("%Y-%m-%d")
title = "Penguin Univeristy"
title_middle = title.title()
main_menu_teacher = f"""
						o> {title_middle} <o
													{tanggal_sekarang}
   Main Menu :

   <A> Students' Data
   <B> Teacher's Data
   <C> Drop Out
   <D> Update Student's Data
   <E> Attendance
   <F> Attendance List
   <G> Searching for Specific Student's Data
   <H> Change Password
   <I> About school
   <J> About this app
   <Q> Quit
"""

main_menu_student = f"""
						o> {title_middle} <o
													{tanggal_sekarang}
   Main Manu : 

   <A> Students' Data
   <B> Teacher's Data
   <C> Attendance
   <D> Attendance List
   <E> Searching for Specific Student's Data
   <F> Change Password
   <G> About this app
   <I> About school
   <Q> Quit
"""

main_menu_enroller = f"""
						o> {title_middle} <o
													{tanggal_sekarang}
   Main Menu :

   <A> Enroll
   <B> Teachers' Data
   <C> Students' Data
   <D> Price List
   <E> Searching for Specific Student's Data
   <F> About this app
   <I> About school
   <Q> Quit
"""

def tampilkan_menu_teacher_and_main_menu_answer():
   global teacher_answer
   while True:
      os.system("cls")
      print(main_menu_teacher)
      teacher_answer = str(input("o> Your Answer :"))
      if teacher_answer.capitalize()  == "A":
         students_data.kerja()
      elif teacher_answer.capitalize() == "C":
         dropout.dropout()
      elif teacher_answer.capitalize() == "D":
         update_data.update()
      elif teacher_answer.capitalize() == "G":
         searching.search()
      elif teacher_answer.capitalize() == "J":
         aboutapp.aboutapp()
      elif teacher_answer.capitalize() == "H":
         forgotpasswordteacher.tempat()
      elif teacher_answer.capitalize() == "I":
         aboutschool.aboutschool()
      elif teacher_answer.capitalize() == "E":
         attendance_teacher.attendance()
      elif teacher_answer.capitalize() == "F":
         teacher_attendancelist.attend()
      elif teacher_answer.capitalize() == "B":
         Teacher_Data.data()
      elif teacher_answer.capitalize() == "Q":
         break

def tampilkan_menu_student_and_main_menu_answer():
   global student_answer
   while True:
      os.system("cls")
      print(main_menu_student)
      student_answer = str(input("o> Your Answer :"))
      if student_answer.capitalize()  == "A":
         students_data.kerja()
      elif student_answer.capitalize() == "C":
         attendance_student.attendance()
      elif student_answer.capitalize() == "D":
         studentattendancelist.attend()
      elif student_answer.capitalize() == "E":
         searching.search()
      elif student_answer.capitalize() == "G":
         aboutapp.aboutapp()
      elif student_answer.capitalize() == "F":
         forgotpasswordstudent.tempat()
      elif student_answer.capitalize() == "I":
         aboutschool.aboutschool()
      elif student_answer.capitalize() == "B":
         Teacher_Data.data()
      elif student_answer.capitalize() == "Q":
         break

def tampilkan_menu_enroller_and_main_menu_answer():
   global enroller_answer
   while True:
      os.system("cls")
      print(main_menu_enroller)
      enroller_answer = str(input("o> Your Answer :"))
      if enroller_answer.capitalize()  == "A":
         enroll.enroll_student()
      elif enroller_answer.capitalize() == "D":
         pricelist.enroll_student()
      elif enroller_answer.capitalize() == "C":
         students_data.kerja()
      elif enroller_answer.capitalize() == "E":
         searching.search()
      elif enroller_answer.capitalize() == "I":
         aboutschool.aboutschool()
      elif enroller_answer.capitalize() == "B":
         Teacher_Data.data()
      elif enroller_answer.capitalize() == "F":
         aboutapp.aboutapp()
      elif enroller_answer.capitalize() == "Q":
         break