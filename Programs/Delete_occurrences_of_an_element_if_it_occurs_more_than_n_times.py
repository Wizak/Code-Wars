def delete_nth(order, max_e):
	max_element = list(set(order))[[order.count(i) for i in set(order)].index(max([order.count(i) for i in set(order)]))]
	while True:
		if order.count(max_element) == 0:
			break
		else:
			order.remove(max_element)
	return order + [max_element for _ in range(max_e)]


print(delete_nth([20,37,20,21,21,20], 1))