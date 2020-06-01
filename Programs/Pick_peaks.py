def pick_peaks(arr):
	pos, peaks = [], []
	new_arr = [-1 if arr[i] == arr[i+1] else arr[i] for i in range(len(arr)-1)] + [arr[-1]]

	for i in range(new_arr.count(-1)):
		new_arr.remove(-1)
		print(new_arr)
		
	for i in range(len(arr)-1):
		if arr[i] == arr[i+1]:
			continue
		else:
			new_arr.append(arr[i])
	new_arr.append(arr[-1])

	for i in range(len(arr)):

		if 0 < i < len(arr)-1:
			if arr[i-1] < arr[i] > arr[i+1]:
				pos.append(i)
				peaks.append(arr[i])

	return {'pos':pos, 'peaks':peaks}


arr = [1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]

print(pick_peaks(arr))