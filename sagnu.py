# def main(a,b):
#     if a%2 == 0 and b%2 == 0:
#         if a > b:
#             result = a
#         else:
#             result = b
#     else:
#         if a<b:
#             result = a
#         else:
#             result = 'b'

#     return result 

# def main(a,b):
#     if a%2 == 0 and b%2 == 0:
#         return min(a,b)
#     else:
#         return max(a,b)
def names(text):
    word = text.split()

    return word[0][0] == word[1][0]