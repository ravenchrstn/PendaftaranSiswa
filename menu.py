import os
from datetime import datetime
from main_menu import students_data
import dropout
import load

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
   <B> Attendence
   <C> Searching for Specific Student's Data
   <D> About this app
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
         if len(students_data)
         students_data.kerja()
      if teacher_answer.capitalize() == "B":
         dropout.dropout()


def tampilkan_menu_student_and_main_menu_answer():
   global student_answer
   os.system("cls")
   print(main_menu_student)
   student_answer = input("o> Your Answer :")

def tampilkan_menu_enroller_and_main_menu_answer():
   global enroller_answer
   os.system("cls")
   print(main_menu_enroller)
   enroller_answer = input("o> Your Answer :")

