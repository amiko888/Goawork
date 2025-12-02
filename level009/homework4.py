def is_palindrome(text):
    if text == text[::-1]:
        print('this text is palindrome')
    else:
        print('this text is not palindrome')

is_palindrome('level')
is_palindrome('hello')