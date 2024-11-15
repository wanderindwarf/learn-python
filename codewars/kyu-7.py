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


# LIST FILTERING

# 1.
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