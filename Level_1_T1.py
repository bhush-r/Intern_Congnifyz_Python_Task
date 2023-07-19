"""function that takes a string as input and 
returns the reverse of that string: """

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

"""function by passing a string as an argument and 
it will return the reversed version of that string"""

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
