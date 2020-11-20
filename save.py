from json import dump
import load

def save_data_murid():
	with open("data/students_data.json", "w") as data:
		dump(load.data, data)

def save_data_login():
	with open("data/user_login.json", "w") as datanya:
		dump(load.datalogin, datanya)

def save_data_hadir():
	with open("data/attendance.json", "w") as datanyo:
		dump(load.attendance, datanyo)