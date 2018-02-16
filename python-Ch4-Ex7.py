#Nick Zapata - Ch4 - ex7 - 2/16/18

def computergrade(score):
	score = float(score)
	if score < 0.6:
		print('F')
	elif score >= 0.9:
		print('A')
	elif score >= 0.8:
		print('B')
	elif score >= 0.7:
		print('C')
	elif score >= 0.6:
		print('D')
	else:
		print ('WHAT?')
		
grade = input('Enter a score between 0.0 and 1.0: ')
try:
	if (float(grade) >= 0) and ( float(grade) <= 1 ) :
		computergrade(grade)
	else:
		print (error_msg_invalid)
		
except:
	print (error_msg_invalid)