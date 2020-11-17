def verify():
	verify_answer = print(
	"""
Are you sure ?
[A]. Yes
[B]. No
	""")
	verify_ans = input("Your Answer :")
	if verify_ans.capitalize() == "A":
		return True
	elif verify_ans.capitalize() == "B":
		input("Press Enter to go back to Main Menu")
		return False

