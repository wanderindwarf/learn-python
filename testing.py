# for i in range(2, 8):
#     print("The value of i is currently", i)


##########


# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)

# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# print(my_list)


##########


# my_list_2 = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# unique_list = []

# for number in my_list_2:
#     if number not in unique_list:
#         unique_list.append(number)
#     else:
#         continue

# print("The list with unique elements only:")
# print(unique_list)


##########


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


##########


# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product


# for n in range(1, 6):  # testing
#     print(n, factorial_function(n))


# def factorial_function(n):
#     if n < 0: return None
#     if n < 2: return 1
#     return factorial_function(n-1) * n


# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# def fib(n):
#     if n < 1: return None
#     if n < 3: return 1
#     return fib(n-1) + fib(n-2)
# school_class = {}


##########


# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
    
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)


##########


# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     print(item)
#     d3.update(item)

# print(d3)


##########


# from platform import *


# print(machine(), platform(), processor(), system(), version(), python_implementation(), python_version_tuple(), sep="\n")


##########


# import sys


# sys.path.insert(0, '/home/rekun/python/learning/python-institute-projects/package-experiment/extrapack.zip')


# import extra.good.best.sigma as sigma
# import extra.good.best.tau as tau

# print(sigma.funS(), tau.funT(), sep="\t")


##########


# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False


##########

# numbers = {
#     '1': ["#", "#", "#", "#", "#"],
#     '2': ["###", "  #", "###", "#  ", "###"],
#     '3': ["###", "  #", "###", "  #", "###"], 
#     '4': ["# #", "# #", "###", "  #", "  #"],
#     '5': ["###", "#  ", "###", "  #", "###"],
#     '6': ["###", "#  ", "###", "# #", "###"],
#     '7': ["###", "  #", "  #", "  #", "  #"],
#     '8': ["###", "# #", "###", "# #", "###"],
#     '9': ["###", "# #", "###", "  #", "###"],
#     '0': ["###", "# #", "# #", "# #", "###"]
# }

# user_numbers = input()

# for row in range(5):
#     output = []
#     for number in user_numbers:
#         output.append(numbers[number][row])
#     print(' '.join(output))



# IBAN Validator.

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")


# CAESAR CIPHER

# check = False

# while not check:
#     user_text = input("User text: ")
#     if not user_text.isalnum():
#         check = True

# step = input("Step: ")
# output = ''

# for char in user_text:
#     if char.isalpha():
#         if 90 - int(step) < ord(char) <= 96: output += chr(ord(char) + int(step) - 26)
#         elif 122 - int(step) < ord(char): output += chr(ord(char) + int(step) - 26)
#         else: output += chr(ord(char) + int(step))
#     else:
#         output += char

# print(''.join(output))

#############   OOP WAY


# def char_shift(char, shift):
#     base = ord('a') if char.islower() else ord('A')
#     shifted = (ord(char) - base + shift) % 26

#     return chr(base + shifted) if char.isalpha() else char

# def encryption(text, shift):
#     return ''.join(char_shift(char, shift) for char in text)

# def get_shift():
#     while True:
#         try:
#             shift = int(input("Enter shift (1 - 25): "))
#             if 1 <= shift <= 25: 
#                 return shift
#             print("Shift must be between 1 and 25.")
#         except ValueError:
#             print("Please enter valid integer.")

# def main():
#     text = input("Enter text to ecrypt: ")
#     shift = get_shift()

#     output = encryption(text, shift)

#     print("Encrypted message:", output)


# if __name__ == "__main__":
#     main()


# PALINDROME CHECKER


# def is_palindrome(text):
#     return text[::-1].replace(' ', '').lower() == text.replace(' ', '').lower()

# text = input("Enter palidrome: ")
# print(is_palindrome(text))


# ANAGRAM CHECKER


# def is_anagram(text, text2):
#     for char in text.lower():
#         if char not in text2.lower():
#             return False
#     return True

# text, text2 = input("text1: "), input("text2: ")

# print(is_anagram(text, text2))


# DIGIT OF LIFE

# def get_date():
#     while True:
#         date = input("Enter date (DDMMYYYY): ")
#         if len(date) == 8:
#             return date
#         print("Must be length of 8.")

# def digit_of_life(date):
#     list_of_numbers = [int(number) for number in date]
#     return sum(list_of_numbers) if sum(list_of_numbers) < 10 else sum(list_of_numbers) % 10 + sum(list_of_numbers) // 10

# date = get_date()
# print(digit_of_life(date))


### FIND A WORD

# def comparing(indexes):
#     for index in range(len(indexes) - 1):
#         if indexes[index] > indexes[index + 1]:
#             return False
#     return True

# def indexes(word1, word2):
#     indexes = [word2.find(char) for char in word1]
#     if -1 in indexes:
#         return False
#     print(indexes)
#     return comparing(indexes)

# word1 = input("Word to find: ")
# word2 = input("Letters: ")

# print(indexes(word1, word2))


# SUDOKU VALIDATOR

def has_duplicate(table):
    for array in table:
        unique = []
        for element in array:
            if element in unique:
                return True
            unique.append(element)

def get_input():
    table = ['295743861', '431865927', '876192543', '387459216', '612387495', '549216738', '763524189', '928671354', '154938672']
    # for _ in range(9):
    #     array = input("Enter line of 9 unique numbers: ")
    #     table.append(array)
    return table

def make_columns(table):
    table_of_columns = []
    for element in range(9):
        table_of_columns.append(''.join([table[row][element] for row in range(9)]))
    return table_of_columns

def make_squares(table):
    square = []
    for i in range(0, 9, 3):
        for e in range(0, 9, 3):
            square.append(table[i][e:e+3] + table[i + 1][e:e+3] + table[i + 2][e:e+3])
    return square

def main():

    table = get_input()

    if has_duplicate(table): print(False)
    elif has_duplicate(make_columns(table)): print(False)
    elif has_duplicate(make_squares(table)): print(False)
    else: print(True)

if __name__ == "__main__":
    main()