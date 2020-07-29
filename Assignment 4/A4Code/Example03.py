def main():
	my_dict = {"a": 4, "b": 6, "c": 5}
	for letter in my_dict.keys():
		print(letter)
	for number in my_dict.values():
		print(number)
	for item in my_dict.items():
		print(item)
	for k,v in my_dict.items():
		print(k,v)
	for key in my_dict:
		print(key)


	items_list = list(my_dict.items())
	keys_list = list(my_dict.keys())
	values_list = list(my_dict.values())

	print("items list", items_list)
	print("keys list", keys_list)
	print("values list", values_list)
	
main()