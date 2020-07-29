"""
Assignment 4 Questions - Use this program to develop the assignment 4 functions
"""
import string

def get_phone_number(word_str):
    numpad_dict={'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}
    new_number = ""
    for number in word_str:
        if number in numpad_dict:
            new_number += str(numpad_dict[number])
        else:
            new_number += number
    return new_number 

def test_get_phone_number():
    print(get_phone_number('0800painter'))
    print(get_phone_number('0800fixnow'))
    print(get_phone_number('0800myapple'))

def print_most_numbers_occurrences(numbers_str):
    num_list = numbers_str.split()
    occurance = {}
    
    for number in num_list:
        if int(number) in occurance:
            occurance[int(number) ] += 1
        else:
            occurance[int(number) ] = 1
    max_var = 0,0
    for number,factor in occurance.items():
        if factor > max_var[1]:
            max_var = number,factor
    max_list = ""
    for number,factor in occurance.items():
        if factor == max_var[1]:
            max_list += str(number) + "\n"
    print(max_list) 

def test_print_most_numbers_occurrences():
    print_most_numbers_occurrences('2 3 40 1 5 4 3 3 9  9')
    print_most_numbers_occurrences('9 30 3 9 3 1 4')
    print_most_numbers_occurrences('19 30 13 4 9 3 1 4')

def get_keywords_occurrences(filename):
    document = open(filename,"r")
    document_content = document.read()
    document_list = document_content.split()
    keywords_list = {"and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "False", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "print", "raise", "return", "True", "try", "while", "with", "yield"}
    keywords_dict = {}
    for number in document_list:
        if number in keywords_list:
                if number in keywords_dict:
                        keywords_dict[number] += 1
                else:
                    keywords_dict[number] = 1
                    
    
    return keywords_dict

def test_get_keywords_occurrences():
    keywords_dict = get_keywords_occurrences('Hello.py')
    for key in sorted(keywords_dict):
        print (key, ':', keywords_dict[key])
    keywords_dict = get_keywords_occurrences('Example03.py')
    for key in sorted(keywords_dict):
        print (key, ':', keywords_dict[key])

def get_morse_code_dict(filename):
    file = open(filename, "r")
    file_content = file.read()
    file_list = file_content.split()
    morse_dict = {}
    for element in range(0,len(file_list),2):
        number = file_list[element + 1]
        morse_dict[file_list[element]] = number
    return morse_dict
	
def test_get_morse_code_dict():
    morse_dict = get_morse_code_dict('morse.txt')
    for key in sorted(morse_dict):
        print (key, ':', morse_dict[key])

def words_to_morse(morse_dict, words):
    code_list = []
    for element in words:
        if element in morse_dict:
            code_list.append(morse_dict[element])
    return code_list

def test_words_to_morse():
    print(words_to_morse(get_morse_code_dict('morse.txt'), 'hello'))
    print(words_to_morse(get_morse_code_dict('morse.txt'), 'hello world'))

def get_worst_manufacturer_dict(filename):
    car_file = open(filename,"r")
    car_list = car_file.readlines()
    car_dict = {}
    for car in car_list:
        cars = car.split()
        if cars[1] not in car_dict:
                car_dict[cars[1]] = []
        car_dict[cars[1]].append(cars[0])
    return car_dict 

def test_get_worst_manufacturer_dict():
    car_dict = get_worst_manufacturer_dict('cars_simple.txt')
    for key in sorted(car_dict):
        print (key, ':', car_dict[key])
    car_dict = get_worst_manufacturer_dict('cars.txt')
    for key in sorted(car_dict):
        print (key, ':', car_dict[key])
		
def print_worst_manufacturer(car_dict):
    longest_length = "nothing", []
    for car, vans in car_dict.items():
        if len(vans) > len(longest_length[1]):
            longest_length = car,vans
    print("Worst manufacturer:", longest_length[0]) 

def test_print_worst_manufacturer():
    car_dict = {'Amphicar': ['1961'], 'Corvair': ['1961'], 'Horsey': ['1899'], 'Overland': ['1911'], 'Ford': ['1909', '1958']}
    print_worst_manufacturer(car_dict) 

    car_dict = {'MGA': ['1958'], 'Amphicar': ['1961'], 'Aston': ['1976'], 'Horsey': ['1899'], 'Bricklin': ['1975'], 'Zunndapp': ['1958'], 'Pontiac': ['2001'], 'Chevy': ['1976', '2004'], 'Mosler': ['1985'], 'Lamborghini': ['1986'], 'Peel': ['1966'], 'Ferrari': ['1980'], 'AMC': ['1970', '1978'], 'Yugo': ['1985'], 'BMW': ['2002'], 'Ford': ['1909', '1958', '1971', '1995', '2000'], 'Crosley': ['1949'], 'GM': ['1997'], 'Fuller': ['1933'], 'Chrysler': ['1971'], 'Chrysler/Desoto': ['1934'], 'Corvette': ['1980'], 'Lotus': ['1958'], 'Waterman': ['1957'], 'Overland': ['1911'], 'Triumph': ['1970', '1975'], 'Scripps-Booth': ['1913'], 'King': ['1957'], 'Camaro': ['1982'], 'De': ['1981'], 'Briggs': ['1920'], 'Fiat': ['1998'], 'Corvair': ['1961'], 'Trabant': ['1975'], 'Plymouth': ['1997'], 'Jaguar': ['1974', '2001'], 'Maserati': ['1984'], 'Morgan': ['1975'], 'Hummer': ['2003'], 'Cadillac': ['1981', '1982'], 'Renault': ['1956']}
    print_worst_manufacturer(car_dict)
	
    car_dict ={'MGA': ['1958'], 'Amphicar': ['1961'], 'Aston': ['1976'], 'Horsey': ['1899'], 'Bricklin': ['1975'], 'Zunndapp': ['1958'], 'Pontiac': ['2001'], 'Chevy': ['1976', '2004'], 'Mosler': ['1985'], 'Lamborghini': ['1986'], 'Peel': ['1966'], 'Ferrari': ['1980'], 'AMC': ['1970', '1978'], 'Yugo': ['1985'], 'BMW': ['2002'], 'Crosley': ['1949'], 'GM': ['1997'], 'Fuller': ['1933'], 'Chrysler': ['1971'], 'Chrysler/Desoto': ['1934'], 'Corvette': ['1980'], 'Lotus': ['1958'], 'Waterman': ['1957'], 'Overland': ['1911'], 'Triumph': ['1970', '1975', 1958], 'Scripps-Booth': ['1913'], 'King': ['1957'], 'Camaro': ['1982'], 'De': ['1981'], 'Briggs': ['1920'], 'Fiat': ['1998'], 'Corvair': ['1961'], 'Trabant': ['1975'], 'Plymouth': ['1997'], 'Jaguar': ['1974', '2001'], 'Maserati': ['1984'], 'Morgan': ['1975'], 'Hummer': ['2003'], 'Cadillac': ['1981', '1982'], 'Renault': ['1956']}
    print_worst_manufacturer(car_dict)

def main():
    print("===========\nQuestion 1:")
    test_get_phone_number()
    print("===========\nQuestion 2:")
    test_print_most_numbers_occurrences()
    print("===========\nQuestion 3:")
    test_get_keywords_occurrences()
    print("===========\nQuestion 4:")
    test_get_morse_code_dict()
    print("===========\nQuestion 5:")
    test_words_to_morse()
    print("===========\nQuestion 6:")
    test_get_worst_manufacturer_dict()
    print("===========\nQuestion 7:")
    test_print_worst_manufacturer()

main()
	
