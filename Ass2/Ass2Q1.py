
def Remove(duplicate):
	final_list = []
	for num in duplicate:
		if num not in final_list:
			final_list.append(num)
	return final_list
	
duplicate = [5,7,8,9,5,7,3,8]
print(Remove(duplicate))
