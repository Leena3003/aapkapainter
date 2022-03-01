int_list = [1, 2, 3,2, 1]


# length = eval(input("Enter length of array: "))
# int_list = []
# for i in range(length):
# 	integer = input("Enter integer: ")
# 	int_list.append(integer)

def first_duplicate(int_list):
	unique = {}
	for data in int_list:
		if data  not in unique.keys():
			unique[data] = 1
		else:
			print(data)
			break

first_duplicate(int_list)