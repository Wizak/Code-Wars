# def meeting_time(Ta, Tb, r):
# 	if Ta != 0 and Tb != 0:
# 		if len(str(round(abs(Ta*Tb/(Ta - Tb)), 4))[str(round(abs(Ta*Tb/(Ta - Tb)), 4)).index('.')+1:]) == 1:
# 			return str(round(abs(Ta*Tb/(Ta - Tb)), 4))+'0'
# 	elif Ta == 0:
# 		return str(Tb)+'.00'
# 	elif Tb == 0:
# 		return str(Ta)+'.00'


def meeting_time(Ta, Tb, r):
	return "{:.2f}".format(abs(Ta * Tb / (Tb - Ta))) if Tb != Ta != 0 else "{:.2f}".format(abs(Ta + Tb))

if __name__ == '__main__':

	Ta, Tb, r = 12, -15, 6

	print(meeting_time(Ta, Tb, r))