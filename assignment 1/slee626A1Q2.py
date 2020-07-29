"""
Name: Se Ho Lee
Username: slee626
Student Id: 890218467
Description: A program which encrypts a five letter word.(4 marks)     
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
scrambled_alphabet = "updvcslymkxzfrejnaowhgbqit"
title = "A Simple Encrypter"
extra = 1
title_length = len(title)
border_line = title_length + extra * 2

print("#" * border_line)
print("#" * extra + title + extra * "#")
print("#" * border_line)
print("")

print("Alphabet:", alphabet)
print("Scrambled Alphabet:", scrambled_alphabet)
print("")

five_letter_word = input("Please enter a 5 letter word: ")
first_letter = five_letter_word[0]
second_letter = five_letter_word[1]
third_letter = five_letter_word[2]
fourth_letter = five_letter_word[3]
last_letter = five_letter_word[4]

first_letter_found_position = scrambled_alphabet.find(first_letter)
second_letter_found_position = scrambled_alphabet.find(second_letter)
third_letter_found_position = scrambled_alphabet.find(third_letter)
fourth_letter_found_position = scrambled_alphabet.find(fourth_letter)
last_letter_found_position = scrambled_alphabet.find(last_letter)

new_first_letter_position = alphabet[first_letter_found_position]
new_second_letter_position = alphabet[second_letter_found_position]
new_third_letter_position = alphabet[third_letter_found_position]
new_fourth_letter_position = alphabet[fourth_letter_found_position]
new_last_letter_position = alphabet[last_letter_found_position]

new_first_letter = new_first_letter_position
new_second_letter = new_second_letter_position
new_third_letter = new_third_letter_position
new_fourth_letter = new_fourth_letter_position
new_last_letter = new_last_letter_position

print("Encrypted word: ", new_first_letter, new_second_letter, new_third_letter, new_fourth_letter, new_last_letter, sep = "")
