
def main():
    print('Test values without rounding problems.')
    test_values = '0.75 0.1 0.3333333333333333333333333333'.split()
    significant = [1, 2, 4, 10]

    for value in test_values:
        print('Decimal:', value)
        for digits in significant:
            print(digits, 'sig digit/s:')
            fraction_to_binary(value, digits)
    print()

def fraction_to_binary(fraction_string, significant_binary_digits):
    number_string = ""
    number_list = []
    fraction_string = float(fraction_string)
    while fraction_string != 1:
        if fraction_string < 1:
            fraction_string = fraction_string * 2
            if fraction_string < 1:
                number_list += [0]
        elif fraction_string > 1:
            number_list += [1]
            fraction_string -= 1
    number_list += [1]
    number_index = number_list.index(1)
    list_length = len(number_list[number_index + 1:])
    if significant_binary_digits > list_length:
        number_list += (significant_binary_digits- list_length) * [0]
    else:
        number_list = number_list[:number_index + significant_binary_digits + 1]
    for value in number_list:
        print(value, end = " ")
    print()
    
    if number_list[number_index + significant_binary_digits] == 1:
        number_list[number_index + significant_binary_digits] += 1
    while number_list[0] != 2 and 2 in number_list:
        number_index2 = number_list.index(2)
        number_list[number_index2] = 0
        number_list[number_index2 - 1] += 1
    
    if number_list[0] == 2:
        number_list[0] = 0
        number_list = [1] + number_list 
    else:
        number_list = [0] + number_list 
    
    number_index = number_list.index(1)  
    list_length = len(number_list[number_index + 1:])
    if significant_binary_digits - 1 > list_length:
        number_list += (significant_binary_digits - list_length) * [0]
    else:
        number_list = number_list[:number_index + significant_binary_digits]
    
    for value in number_list:
        number_string += str(value)
    number_string = number_string[0] + "." + number_string[1:]
    print(number_string)
main()

            
