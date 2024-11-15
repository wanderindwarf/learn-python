# EVEN OR ODD

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