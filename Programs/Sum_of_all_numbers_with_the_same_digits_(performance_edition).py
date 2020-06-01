def sum_arrangements(num):

	nums = [i for i in str(num)]
	new_nums = []

	while True:
		for j in range(len(nums)):
			if j+1 < len(nums):
				a, b = nums[j], nums[j+1]
				nums[j], nums[j+1] = b, a
				print(nums)
				new_nums.append(nums.copy())	

		if int(''.join(new_nums[-1])) == num:
			return sum([int(''.join(i)) for i in new_nums])

num = 1185

print(sum_arrangements(num))