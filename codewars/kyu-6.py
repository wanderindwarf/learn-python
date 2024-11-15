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