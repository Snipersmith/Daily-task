def get_month_quarter(number):
	month = 12

	if month >= 1 and month <= 3:
		return 1
	elif month >= 4 and month <= 6:
		return 2
	elif month >= 7 and month <= 9:
		return 3
	elif month >= 10 and month <= 12:
		return 4


print(month)