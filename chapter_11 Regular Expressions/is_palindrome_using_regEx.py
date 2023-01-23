import re


def is_palindrome(phrase):
    forward = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forward[::-1]
    return forward == backwards


phrase = "Hello World"
print(f"This phrase is palindrome: {is_palindrome(phrase)}")
phrase = "Go hang a salami - I'm a lasagna hog."
print(f"This phrase is palindrome: {is_palindrome(phrase)}")