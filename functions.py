def multipy(x, y):
    x_y = x * y
    return x_y


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


word = input("Please enter the world to check: ")
if is_palindrome(word):
    print("'{}' is plaindrome".format(word))
else:
    print("'{}' is not palindrome".format(word))

# answer = multipy(10,45)
# print(answer)


# a_b = multipy(4,8)
# print(a_b)R

# for pav in range(1,6):
#     van = multipy(6,pav)
#     print(van)
