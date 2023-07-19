import re

def is_valid_email(email):
    """
    Validates an email address.
    :param email: The email address to validate.
    :return: True if the email address is valid, False otherwise.
    This function validates an email address by checking if it matches a regular expression pattern.
    """
    # Email pattern for basic validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$' #(string1)@(string2).(2+characters)

    """
    The regular expression pattern matches any string that starts with a word character or a hyphen,
    followed by zero or more word characters, hyphens, or periods, followed by an @ symbol,
    followed by zero or more word characters, hyphens, or periods, followed by a domain name,
    followed by a top-level domain. The top-level domain must be two or more characters long and consist of only letters or numbers.
    """

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")












































# import re

# def is_valid_email(email):
#     # Email pattern for basic validation
#     pattern = r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#     # Check if the email matches the pattern
#     if re.match(pattern, email):
#         # Check if the domain name is valid
#         domain = email.split('@')[1]
#         if not re.match(r'[a-zA-Z0-9]+\.[a-zA-Z]{2,}$', domain):
#             return False

#         return True
#     else:
#         return False

# email = input("Enter an email address: ")
# if is_valid_email(email):
#     print("Valid email address")
# else:
#     print("Invalid email address")





