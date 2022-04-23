def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    return string[::-1].casefold() == string.casefold()


word = input("Please enter the word: ")
if palindrome_sentence(word):
    print("{} is palindrome".format(word))

else:
    print("{} is not palindrome".format(word))
