from json import load

with open("data/students_data.json", "r") as makan:
	data = load(makan)
with open("data/user_login.json", "r") as datanya:
	datalogin = load(datanya)
with open("data/attendance.json", "r") as datamu:
	attendance = load(datamu)
with open("data/teachers_data.json", "r") as datam:
	data_guru = load(datam)
