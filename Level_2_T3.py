import string
import getpass

def check_pass_strength():
    password = getpass.getpass('Enter your new password: ')
    strength = 0
    message = ''

    for char in password:
        if char in string.ascii_lowercase:
            strength += 1
        elif char in string.ascii_uppercase:
            strength += 1
        elif char in string.digits:
            strength += 1
        else:
            strength += 1

    if len(password) >= 8:
        strength += 1

    if strength == 1:
        message = 'Your password is very weak.'
    elif strength == 2:
        message = 'Your password is weak.'
    elif strength == 3:
        message = 'Your password is moderate. add special characters.'
    elif strength == 4:
        message = 'Your password is strong! Your account is well protected.'
    else:
        message = 'Your password does not meet the minimum requirements. Please try again.'

    return message

if __name__ == "__main__":
    print("Welcome to Cognifyz the Password Strength Checker!")
    print("password mix of uppercase and lowercase letters, digits, and special characters.")
    print("it should be at least 8 characters long.")
    
    while True:
        password_strength = check_pass_strength()
        print(password_strength)

        choice = input("Do you want to try another password? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("Thank you for using the Password Strength Checker. Stay secure!")
