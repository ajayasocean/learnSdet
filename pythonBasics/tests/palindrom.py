"""
Palindrome algorithm
Read the number or letter.
Hold the letter or number in a temporary variable.
Reverse the letter or number.
Compare the temporary variable with reverses letter or number.
If both letters or numbers are the same, print "this string/number is a palindrome."
Else print, "this string/number is not a palindrome."
"""
# taking input from user
user_input = input('Please enter a string:\n')


def check_palindrome(user_input):
    reversed_user_input = user_input[::-1]
    if reversed_user_input == user_input:
        print(user_input, '\t is a palindrome')
    else:
        print(user_input, '\t is not a palindrome')


check_palindrome(user_input)
