
def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1: -1]


def is_palindrome(word):
    """Check whether a word is a palindrome."""
    if first(word) != last(word):
        return False
    if not middle(word):
        return True
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))


