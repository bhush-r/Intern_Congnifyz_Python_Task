#create a function
def palindrome(string):
    
#Returns bool: True if the string is a palindrome, False otherwise.
    
    reversed_string = string[::-1]
    return string == reversed_string

# User to enter a string and check whether it is a palindrome
string = input("Enter a string: ")
if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
