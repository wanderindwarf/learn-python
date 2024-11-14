# def filter_list(list):
#     return [element for element in list if type(element) != str]


# DESCENDING ORDER
# 1.
# def descending_order(number):
#     number = list(str(number))
#     swap = True
#     while swap:
#         swap = False
#         for i in range(len(number) - 1):
#             if number[i] < number[i + 1]:
#                 swap = True
#                 number[i], number[i + 1] = number[i + 1], number[i]
#     return number

# 2.
# def descending_order(number):
#     number_list = list(str(number))
#     number_list.sort(reverse=True)
#     return int(''.join(number_list))

# 3.
# def descending_order(number):
#     return ''.join(sorted(str(number), reverse=True))


# REVERSED STRINGS

# 1.
# def solution(string):
#     string = list(string)
#     for i in range(len(string) // 2):
#         string[i], string[-i - 1] = string[-i - 1], string[i]
#     return ''.join(string)

#2.
# def solution(string):
#     return string[::-1]   # using list slicing list[Initial : End : IndexJump]


# DUPLICATE ENCODER

# 1.
# def duplicate_encode(word):
#     no_duplicates_list = []
#     duplicates_list = []
#     output = ''
#     word = word.lower()
#     for char in word:
#         if char not in no_duplicates_list:
#             no_duplicates_list.append(char)
#         else:
#             duplicates_list.append(char)
#     for char in word:
#         if char in duplicates_list:
#             output += ')'
#         else:
#             output += '('
#     return output

# 2.
# def duplicate_encode(word):
#     return ''.join([')' if word.lower().count(char) > 1 else '(' for char in word.lower() ])


# REMOVE FIRST AND LAST CHARACTER

# 1.
# def remove_char(s):
#     return ''.join(s[1:-1])


# REMOVE FIRST AND LAST CHARACTER (PART TWO)

# 1.
# def array(string):
#     element = ''
#     output = []
#     for char in string:
#         if char not in ", ":
#             element += f'{char}'
#         elif char == ',':
#             output.append(element)
#             element = ''
#     if len(output) <= 1:
#         return None
#     return " ".join(output[1:])

# 2.
# def array(strng):
#     return ' '.join(strng.split(',')[1:-1]) or None


# EXES AND OHS

# 1.
# def xo(s):
#     x, o = 0, 0
#     for char in s.lower():
#         if char == 'x':
#             x += 1
#         if char == 'o':
#             o += 1
#     return x == o

# 2.
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

# 3. (will I ever understand this?)
# import re

# # Using regex, the number of x's and o's are extracted from the test string
# # and returned as a tuple.
# def get_amounts(test):
#     return(len(re.findall("[Xx]", test)), len(re.findall("[Oo]", test)))

# # The results passed to this function will evaluate to True if they are equal
# # and False if they are not.
# def eval_results(results):
#     if results[0] == results[1]:

#         return True
#     else:

#         return False

# # Call the get_amounts( ... ) and eval_results( ... ) functions and return the
# # result.
# def xo(test):
#     result = get_amounts(test)
#     return eval_results(result)


# HOW GOOD ARE YOU REALLY?

# 1.
# def better_than_average(class_points, your_points):
#     sum_of_points = 0
#     for point in class_points:
#         sum_of_points += point
#     return your_points > sum_of_points // len(class_points)

# 2.
# def better_than_average(class_points, your_points):
#     return your_points > sum(class_points) / len(class_points)


# CALCULATE BMI

# 1.
# def bmi(weight, height):
#     bmi = weight / height ** 2
#     if bmi <= 18.5: return "Underweight"
#     elif bmi <= 25.0: return "Normal"
#     elif bmi <= 30.0: return "Overweight"
#     else: return "Obese"

# 2. (List comprehention and smart use of Logical "1" for list indexing)
# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]


# EVEN OR ODD (8 KYU)

# 1.
# def even_or_odd(number):
#     if number % 2 == 0: return "Even"
#     else: return "Odd"

# 2.
# def even_or_odd(number):
#     return "Odd" if number % 2 else "Even"

# 3.
# def even_or_odd(number):
#     return ["Even", "Odd"][number % 2]


# CONVERT STRING TO NUMBER

# 1.
# def string_to_number(s):
#     return int(s)

# 2.
# string_to_number = int


# TIC-TAC-TOE-SOLVER (5 KYU)

# 1.
# def is_solved(board):
#     for i in range(3):
#         if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
#             if board[i][i] != 0: return board[i][i]
#     if board[0][0] == board[1][1] == board[2][2] or board[2][0] is board[1][1] is board[0][2]:
#         if board[1][1] != 0: return board[1][1]
    
#     for i in range(3):
#         if board[i][0] == 0 or board[i][1] == 0 or board[i][2] == 0: return -1 
#     return 0

# 2.
# def is_solved(board):
#     UNFINISHED = -1
#     DRAW = 0

#     array = [row[i] for i in range(3) for row in board]

#     combinations = [(i, i + 1, i + 2) for i in range(0, 7, 3)] + \
#                    [(i, i + 3, i + 6) for i in range(3)] + \
#                    [(0, 4, 8), (2, 4, 6)]

#     for e in combinations:
#         if array[e[0]] is array[e[1]] is array[e[2]] is not DRAW: return array[e[0]]

#     return UNFINISHED if 0 in array else DRAW


# SENTENCE SMASH (8 KYU)

# 1.
# def smash(words):
#     return ' '.join(words)

# 2.
# smash = ' '.join


# OPPOSITES ATTRACT

# 1.
# def lovefunc( flower1, flower2 ):
#     return bool(flower1 % 2 ^ flower2 % 2)

# 2.
# def lovefunc( flower1, flower2 ):
#     return flower1 & 1 ^ 1 & flower2


# GRASSHOPPER - SUMMATION

# 1.
# def summation(num):
#     if num == 1: return 1
#     else: return num + summation(num-1)


# 2.
# def summation(num):
#     return (1+num) * num / 2


# TWO TO ONE

# 1.
# def longest(a1, a2):
#     long_string = ''
#     for letter in a1 + a2:
#         if letter not in long_string:
#             long_string += letter
#     return ''.join(sorted(long_string))

# 2.
# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))




