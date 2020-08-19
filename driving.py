country = input('請輸入您的國家: ')
age = input('請輸入您的年齡: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('您可以考取駕照')
	else:
		print('您還無法考取駕照')
elif country == 'USA':
	if age >= 16:
		print('您可以考取駕照')
	else:
		print('您還無法考取駕照')
else:
	print ('您只能輸入Taiwan / USA')
