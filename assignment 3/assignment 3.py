#--------------------------------------------------
#Main function
#--------------------------------------------------
def main():
    user_selection = 1
    while user_selection >= 1 and user_selection <= 7:
        print()
        user_selection = get_user_selection()
        print()
        if user_selection == 1:
            print_header(1, "test_get_last_two_letters()")
            test_get_last_two_letters()
        elif user_selection == 2:
            print_header(2, "test_get_longest_word()")
            test_get_longest_word()	
        elif user_selection == 3:
            print_header(3, "test_get_negatives_at_front()")
            test_get_negatives_at_front()
        elif user_selection == 4:		
            print_header(4, "test_is_legitmate_code()")
            test_is_legitmate_code()
        elif user_selection == 5:		
            print_header(5, "test_get_common_words_used()")
            test_get_common_words_used()	
        elif user_selection == 6:
            print_header(6, "test_remove_triples()")
            test_remove_triples()
        elif user_selection == 7:
            print_header(7, "test_get_hand_score()")
            test_get_hand_score()
        print()

def get_user_selection():
    print('   ', 1, ". test_get_last_two_letters(): ", sep='')
    print('   ', 2, ". test_get_longest_word(): ", sep='')	
    print('   ', 3, ". test_get_negatives_at_front(): ", sep='')
    print('   ', 4, ". test_is_legitmate_code(): ", sep='')		
    print('   ', 5, ". test_get_common_words_used(): ", sep='')			
    print('   ', 6, ". test_remove_triples(): ", sep='')
    print('   ', 7, ". test_get_hand_score(): ", sep='')
    print('   0. Quit: ')
    return int(input("      Enter selection: "))
#--------------------------------------------------
# 7777777777777777777777777777777777777777777777777
# Score a hand of eight random dice throws - 3 marks
#--------------------------------------------------
"""
In a dice rolling game a hand is made up of eight random dice throws and
is valued in the following way:

     Each dice which is part of a run of dice starting from a 1 has a value
        which is equivalent to the dice number. The value of any dice
        which is part of a run is added to the hand score.
     If there is no 1 in a hand of eight dice then the score for the whole hand is 0.
     A hand of dice can contain more than one run.

Study the following five example hands of eight dice and their
corresponding valuation.  Make sure you understand how the hands are
valued:

[5, 3, 2, 5, 5, 6, 4, 3] has value 0
[3, 4, 1, 5, 3, 1, 4, 6] has value 2 (contains one run with just the dice [1]
    and a second run with just [1])
[5, 3, 2, 6, 4, 5, 1, 4] has value 21 (contains one run with the
    dice [1, 2, 3, 4, 5, 6])
[2, 1, 1, 1, 2, 3, 3, 2] has value 15 (contains one run with the
    dice [1, 2, 3], a second run with the dice [1, 2, 3], and
    another run with the dice [1, 2])
[3, 4, 1, 5, 2, 1, 4, 6] has value 22 (contains one run
    with the dice [1, 2, 3, 4, 5, 6], 
    another run with the dice [1])

Complete the get_hand_score() function which is passed a list of eight
dice throws and returns the value of the hand according to the rules
described above.
"""
def get_hand_score(list_of_dice):
    final_list = []
    list_of_dice.sort()
    for number in list_of_dice:
        if number == 1:
            final_list.append(1)
            first_position = list_of_dice.index(1)
            if 2 in list_of_dice:
                second_position = list_of_dice.index(2)
                final_list.append(2)
                list_of_dice.pop(second_position)
                if 3 in list_of_dice:
                    third_position = list_of_dice.index(3)
                    final_list.append(3)
                    list_of_dice.pop(third_position)
                    if 4 in list_of_dice:
                        fourth_position = list_of_dice.index(4)
                        final_list.append(4)
                        list_of_dice.pop(fourth_position)
                        if 5 in list_of_dice:
                            fifth_position = list_of_dice.index(5)
                            final_list.append(5)
                            list_of_dice.pop(fifth_position)
                            if 6 in list_of_dice:
                                sixth_position = list_of_dice.index(6)
                                final_list.append(6)
                                list_of_dice.pop(sixth_position)
    return sum(final_list)  
    

def test_get_hand_score():
    print("1.  score: ", get_hand_score([5, 3, 2, 5, 5, 6, 4, 3]))
    print("2.  score: ", get_hand_score([3, 4, 1, 5, 3, 1, 4, 6]))
    print("3.  score: ", get_hand_score([5, 3, 2, 6, 4, 5, 1, 4]))
    print("4.  score: ", get_hand_score([2, 1, 1, 1, 2, 3, 3, 2])) 
    print("5.  score: ", get_hand_score([3, 4, 1, 5, 2, 1, 4, 6]))
    
    
    list1 = [5, 3, 2, 5, 5, 6, 4, 3]
    print("6.  list: ", list1)
    score1 = get_hand_score(list1)	
    list1.sort()
    print("    list_sorted: ", list1)
    print("    score:", score1)
    print()

    list1 = [5, 3, 2, 6, 4, 5, 1, 4]
    print("7.  list: ", list1)
    list1_sorted = sorted(list1)
    score1 = get_hand_score(list1)
    print("    list_sorted: ", list1_sorted)
    print("    score:", score1)
    print()

    list1 = [2, 1, 1, 1, 2, 3, 3, 2] 	
    print("8.  list: ", list1)
    list1_sorted = sorted(list1)
    score1 = get_hand_score(list1)
    print("    list_sorted: ", list1_sorted)
    print("    score:", score1)
    """
    ------------------------------
    777777777777777777777777777777
    7. test_get_dice_score()
    ------------------------------
    1.  score:  0
    2.  score:  2
    3.  score:  21
    4.  score:  15
    5.  score:  22
    6.  list:  [5, 3, 2, 5, 5, 6, 4, 3]
        list_sorted:  [2, 3, 3, 4, 5, 5, 5, 6]
        score: 0

    7.  list:  [5, 3, 2, 6, 4, 5, 1, 4]
        list_sorted:  [1, 2, 3, 4, 4, 5, 5, 6]
        score: 21

    8.  list:  [2, 1, 1, 1, 2, 3, 3, 2]
        list_sorted:  [1, 1, 1, 2, 2, 2, 3, 3]
        score: 15
    """
#--------------------------------------------------
# 6666666666666666666666666666666666666666666666666
# Remove one element from any three identical 
# sequential elements - 3 marks
#--------------------------------------------------
"""
Define the remove_triples() function which is passed a list of integers
as a parameter. The function removes any element in the list which is
the same as the previous two elements.

For example, the following code:

a_list = [6, 6, 6, 7, 6, 6, 4, 3, 3, 3, 8, 8, 8, 3]
remove_triples(a_list)
print("1.", a_list)

a_list = [1, 1, 1, 4, 4, 4, 1, 1, 1]
remove_triples(a_list)
print("2.", a_list)

a_list = [1, 1, 1, 1, 1, 2]
remove_triples(a_list)
print("3.", a_list)

prints:

1. [6, 6, 7, 6, 6, 4, 3, 3, 8, 8, 3]
2. [1, 1, 4, 4, 1, 1]
3. [1, 1, 2]
"""
def remove_triples(a_list):
    end = -1
    for number in a_list:
        index = a_list.index(number)
        if index < len(a_list) - 2:
            if number == a_list[index + 1] and number == a_list[index + 2]:
                a_list.pop(index)
            elif number == a_list[end] and number == a_list[end - 1] and number == a_list[end - 2]:
                a_list.pop(end)

    return a_list


def test_remove_triples():
    a_list = [6, 6, 6, 7, 6, 6, 4, 3, 3, 3, 8, 8, 8, 3]
    remove_triples(a_list)
    print("1.", a_list)

    a_list = [1, 1, 1, 4, 4, 4, 1, 1, 1]
    remove_triples(a_list)
    print("2.", a_list)

    a_list = [1, 1, 1, 1, 1, 2]
    remove_triples(a_list)
    print("3.", a_list)

    list1 = []
    print("4. Before list:", list1)
    remove_triples(list1)
    print("4. After  list:", list1)
    print()

    list1 = [1, 1, 1, 3, 8, 4, 5, 5, 5]
    print("5. Before list:", list1)
    remove_triples(list1)
    print("5. After  list:", list1)
    """
    ------------------------------
    666666666666666666666666666666
    6. test_remove_triples()
    ------------------------------
    1. [6, 6, 7, 6, 6, 4, 3, 3, 8, 8, 3]
    2. [1, 1, 4, 4, 1, 1]
    3. [1, 1, 2]
    4. Before list: []
    4. After  list: []

    5. Before list: [1, 1, 1, 3, 8, 4, 5, 5, 5]
    5. After  list: [1, 1, 3, 8, 4, 5, 5]
    """
#--------------------------------------------------
# 5555555555555555555555555555555555555555555555555
# Get a list of the common English words used
# in a string of text - 3 marks
#--------------------------------------------------	
"""
Define the get_common_words_used() function which is passed a string of
text and a list of commonly used words as parameters. The function
returns a unique sorted list containing all the words in the parameter
string of text which are present in the list of commonly used words.
The returned list should contain no duplicates and should be sorted (you
MUST use the list method, sort()). The string of text should be
converted to lower case before you do any checking as the commonly used
words are all in lower case.

For example, the following code:

print("1.", get_common_words_used("A bus station is where a bus stops  A train\
   station is where a train stops  On my desk I have a work station", ["a", "is", "i", "on", "the"]))
print("2.", get_common_words_used("It is up to you", ["a", 'up', "go", "it", "on", "the", 'is']))
print("3.", get_common_words_used("Easy come, easy go go go", ["a", "is", "go", "on", "the"]))
print("4.", get_common_words_used("", ["a", "is", "i", "on", "the"]))
print("5.", get_common_words_used("May your coffee be strong and your Monday be short", ["a", "is", "i", "on", "the"]))

prints:

1. ['a', 'i', 'is', 'on']
2. ['is', 'it', 'up']
3. ['go']
4. []
5. []
"""
def get_common_words_used(text, common_words):
    empty_list = []
    text_split = text.split()
    for word in text_split:
        if word.lower() in common_words:
            if word.lower() not in empty_list:
                empty_list.append(word.lower())
        else:
            pass
        
    return sorted(empty_list)

def test_get_common_words_used():
    print("1.", get_common_words_used("A bus station is where a bus stops  A train\
     station is where a train stops  On my desk I have a work station", ["a", "is", "i", "on", "the"]))
    print("2.", get_common_words_used("It is up to you", ["a", 'up', "go", "it", "on", "the", 'is']))
    print("3.", get_common_words_used("Easy come, easy go go go", ["a", "is", "go", "on", "the"]))
    print("4.", get_common_words_used("", ["a", "is", "i", "on", "the"]))
    print("5.", get_common_words_used("May your coffee be strong and your Monday be short", ["a", "is",
                    "i", "on", "the"]))
    
    common_words = ["the", "of", "and", "to", "a", "in", "is", "you", "are",
                    "for", "that", "or", "it", "as", "be", "on", "your", "with",
                    "can", "have", "this", "an", "by", "not", "but", "at",
                    "from", "i", "they", "more"]

    print("6.", get_common_words_used("A bus station is where a bus stops  A train\
     station is where a train stops  On my desk I have a work station", common_words))
    """
    ------------------------------
    555555555555555555555555555555
    5. test_get_common_words_used()
    ------------------------------
    1. ['a', 'i', 'is', 'on']
    2. ['is', 'it', 'up']
    3. ['go']
    4. []
    5. []
    6. ['a', 'have', 'i', 'is', 'on']
    """
#--------------------------------------------------
# 4444444444444444444444444444444444444444444444444
# Returns True if the parameter string is a 
# legitimate code, False otherwise - 3 marks
#--------------------------------------------------	
"""
Define the is_legitmate_code() function which is passed a string as a
parameter. The function returns a boolean indicating whether the
parameter string is a legitimate code or not.  A legitimate code is a
string made up of one letter followed by one or more digits (can also
include spaces before or between the digits).  The first three lines of
code inside the function should be:

code_letters = ["A", "B", "Z", "T", "X"]
min_for_each_letter = [2, 2, 1, 0, 4] #inclusive
max_for_each_letter = [8, 9, 6, 7, 5] #inclusive

where:

code_letters is the list of code letters which are legitimate for the
first letter of the code string, min_for_each_letter is a list which
contains the minimum number (inclusive) for each digit following that
letter, max_for_each_letter is a list which contains the maximum number
(inclusive) for each digit following that letter.

For example, the third element of the code_letters list is the letter
'Z', the corresponding third element of the min_for_each_letter list is
1 and the corresponding third element of the max_for_each_letter list is
6.  This indicates that the code digits which follows the letter 'Z' can
be any number made up of the digits 1, 2, 3, 4, 5 or 6.  The number part
of the code string can also contain any number of spaces.

Note:  The number part of a parameter code string to be tested could
contain an alphabetic character thus making the code not legitimate.
You will find it useful to use the isdigit() method which returns True
if a string is a digit, False otherwise.

For example, the following code:

print("1.", is_legitmate_code('B747346'))
print("2.", is_legitmate_code('X  444  454'))
print("3.", is_legitmate_code('T 444854'))
print("4.", is_legitmate_code('X  444X454'))
print("5.", is_legitmate_code('X  '))
print("6.", is_legitmate_code('C123  ')

prints:

1. True
2. True
3. False
4. False
5. False
6. False
"""
def is_legitmate_code(code_str):	
    code_letters = ["A", "B", "Z", "T", "X"]
    min_for_each_letter = [2, 2, 1, 0, 4] 
    max_for_each_letter = [8, 9, 6, 7, 5]
    letter = code_str[0]
    number = code_str[1:]
    index = 0

    if len(code_str) == 0:
        return False
    if letter not in code_letters:
        return False
    code_index = code_letters.index(letter)
    code_range = list(range(min_for_each_letter[code_index], max_for_each_letter[code_index] + 1))
    a = False
    for value in number:
        if value == " ":
            pass
        elif value.isalpha() == True:
            return False
        elif int(value) not in code_range:
            return False
        else:
            a = True

    return a
    
def test_is_legitmate_code():
    print("1.", is_legitmate_code('B747346'))
    print("2.", is_legitmate_code('X  444  454'))
    print("3.", is_legitmate_code('T 444854'))
    print("4.", is_legitmate_code('X  444X454'))
    print("5.", is_legitmate_code('X  '))
    print("6.", is_legitmate_code('C123  '))

    codes_to_check = ['X45 5', "C-234", 'X5 45 4 4 54', 'B3 2S56 8']
    number = 7

    for code in codes_to_check:
            print(str(number) + ". ", code, ":  ", is_legitmate_code(code), sep = "")
            number = number + 1	
    """
    ------------------------------
    444444444444444444444444444444
    4. test_is_legitmate_code()
    ------------------------------
    1. True
    2. True
    3. False
    4. False
    5. False
    6. False
    7. X45 5:  True
    8. C-234:  False
    9. X5 45 4 4 54:  True
    10. B3 2S56 8:  False
    """
#--------------------------------------------------
# 3333333333333333333333333333333333333333333333333
# Return a list of numbers from the parameter lists
# with all the negative numbers at the front of 
# the list and all the positive numbers at the back - 3 marks
#--------------------------------------------------	
"""
Define the get_negatives_at_front() function which is passed two lists
of integers as parameters, list1 and list2. The two parameter lists do
not necessarily have the same length. The function returns a new list
containing all the elements from both the parameter lists with all the
negative numbers at the front of the list which is returned and all the
positive numbers at the back of the list.

Note that the order of the elements in the returned list is important: 
firstly, the first element of list1 is check: if it is a negative number
it is inserted in the first position of the list to be returned and if
it is a positive number it is inserted into the last position of the
list to be returned. Then the first element of list2 is checked and, if
it is a negative number, it is inserted in the next available position
going up the list to be returned or, if it is negative, it is inserted
in the next available position going down from the end of the list to be
returned. And so on.

If both the parameter lists are empty, the function should return the
empty list. For example, the following code:

list1 = [-1, 2, -3]
list2 = [4, -6, 3]
print("1.", get_negatives_at_front(list1, list2))
print("2.", get_negatives_at_front([1, 2, -3, 4, 7], [4, -6, 3, -1]))
print("3.", get_negatives_at_front([-1, -2, 6], [-5, 1, 2]))
print("4.", get_negatives_at_front([], []))

prints:

1. [-1, -6, -3, 3, 2, 4]
2. [-6, -3, -1, 7, 4, 3, 2, 4, 1]
3. [-1, -5, -2, 2, 6, 1]
4. []
"""
def get_negatives_at_front(list1, list2):
    positive_numbers = []
    negative_numbers = []
    for number in range(min(len(list1), len(list2))):
        if list1[number] > 0:
            positive_numbers.insert(0,list1[number])
        elif list1[number] <0:
            negative_numbers.append(list1[number])
        if list2[number] > 0:
            positive_numbers.insert(0, list2[number])
        elif list2[number] <0:
            negative_numbers.append(list2[number])
    if len(list1) > len(list2):
        for number in range(len(list2),len(list1)):
            if list1[number] > 0:
                positive_numbers.insert(0, list1[number])
            elif list1[number] <0:
                negative_numbers.append(list1[number])
    elif len(list2) > len(list1):
        for number in range(len(list1),len(list2)):
            if list2[number] > 0:
                positive_numbers.insert(0, list2[number])
            elif list2[number] <0:
                negative_numbers.append(list2[number])
    list3 = negative_numbers + positive_numbers
    return list3
    

def test_get_negatives_at_front():
    list1 = [-1, 2, -3]
    list2 = [4, -6, 3]
    print("1.", get_negatives_at_front(list1, list2))
    print("2.", get_negatives_at_front([1, 2, -3, 4, 7], [4, -6, 3, -1]))
    print("3.", get_negatives_at_front([-1, -2, 6], [-5, 1, 2]))
    print("4.", get_negatives_at_front([], []))
    """
    ------------------------------
    333333333333333333333333333333
    3. test_get_negatives_at_front()
    ------------------------------
    1. [-1, -6, -3, 3, 2, 4]
    2. [-6, -3, -1, 7, 4, 3, 2, 4, 1]
    3. [-1, -5, -2, 2, 6, 1]
    4. []
    """
#--------------------------------------------------
# 2222222222222222222222222222222222222222222222222
# Returns the longest word (which has five or more
# characters) from the parameter list - 3 marks
#--------------------------------------------------
"""
Define the get_longest_word() function which is passed a list of strings
as a parameter.  The function returns the word in the list which has the
most characters (i.e., the longest word) BUT only words with five or
more characters are considered.  If two or more words in the list have
the same number of characters as the longest word, the function should
return the last word from the start of the list which has the most
characters.  If the parameter list is empty or if there are no words in
the list with five of more characters, the function should return the
empty string.  For example, the following code:

print("1.", get_longest_word(["Candide", "Jessie", "Kath", "Amity", "Raeann"]))
print("2.", get_longest_word(["Jo", "Jessie", "Penelope", "Jin", "Raeann", "Lesley"]))
print("3.", get_longest_word(["Alan", "Jess", "Amity", "Rosalie", "Raeanne"]))
print("4. ", "***", get_longest_word(["Jo", "Jai", "Jen", "Jing", "Joey", "Jess"]), "***", sep = "")
print("5. ", "***", get_longest_word([]), "***", sep = "")
print("6.", "***" + get_longest_word([""]) + "***")

prints:

1. Candide
2. Penelope
3. Raeanne
4. ******
5. ******
6. ******
"""
def get_longest_word(a_list):	
    minimum_length = 5
    new_word = ""
    for word in a_list:
        if len(word) >= minimum_length and len(word) >= len(new_word):
            new_word = word

    return new_word
            
def test_get_longest_word():
    print("1.", get_longest_word(["Candide", "Jessie", "Kath", "Amity", "Raeann"]))
    print("2.", get_longest_word(["Jo", "Jessie", "Penelope", "Jin", "Raeann", "Lesley"]))
    print("3.", get_longest_word(["Alan", "Jess", "Amity", "Rosalie", "Raeanne"]))
    print("4. ", "***", get_longest_word(["Jo", "Jai", "Jen", "Jing", "Joey", "Jess"]), "***", sep = "")
    print("5. ", "***", get_longest_word([]), "***", sep = "")
    print("6.", "***" + get_longest_word([]) + "***")	
    """
    ------------------------------
    222222222222222222222222222222
    2. test_get_longest_word()
    ------------------------------
    1. Candide
    2. Penelope
    3. Raeanne
    4. ******
    5. ******
    6. ******
    """
#--------------------------------------------------
# 1111111111111111111111111111111111111111111111111
# Get a lowercase string of the last two letters 
# of each word in the parameter list - 2 marks
#--------------------------------------------------
"""	
Define the get_last_two_letters() function which is passed a list of
strings as a parameter. The function returns the string made up of the
concatenation of the last two letters of each words in the parameter
list.  If an element of the list has only one letter then only the one
letter is added to the string to be returned.  The string returned by
the function should be in lowercase characters.  If the parameter list
is an empty list, the function should return an empty string.  For
example, the following code:

print("1.", get_last_two_letters(["Jess", "Cain", "Amity", "Raeann"]))
print("2.", get_last_two_letters(["CAIn", "JessiE", "O", "ROBERT", "Geoffrey", "Li", "B"]))
print("3.", "***" + get_last_two_letters([]) + "***")
print("4.", "***" + get_last_two_letters(["A", "E", "O"]) + "***")

prints:

1. ssintynn
2. inieorteylib
3. ******
4. ***aeo***
"""
def get_last_two_letters(a_list):
    new_word = ""
    for word in a_list:
        new_word += word[-2:].lower()

    return new_word

def test_get_last_two_letters():
    print("1.", get_last_two_letters(["Jess", "Cain", "Amity", "Raeann"]))
    print("2.", get_last_two_letters(["CAIn", "JessiE", "O", "ROBERT", "Geoffrey", "Li", "B"]))
    print("3.", "***" + get_last_two_letters([]) + "***")
    print("4.", "***" + get_last_two_letters(["A", "E", "O"]) + "***")
    """
    ------------------------------
    111111111111111111111111111111
    1. test_get_last_two_letters()
    ------------------------------
    1. ssintynn
    2. inieorteylib
    3. ******
    4. ***aeo***
    """
#--------------------------------------------------
#Print header lines
#--------------------------------------------------	
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)	

main()
