# Question 1
import string 

def validate_password(password: str) -> bool:
    """
    STEP 1: Create a function that validates a password based on the following rules:
        - It must be at least 8 characters long.
        - It must contain at least one uppercase letter.
        - It must contain at least one lowercase letter.
        - It must contain at least one digit.
        - It must contain at least one special character (e.g. @, #, $, %, !).

    TODO: Implement logic to check all these conditions and return True if valid, otherwise False.
    """

    length = False
    upper_case = False
    lower_case = False
    digit = False
    special_character = False

    if not password:
        raise ValueError
    
    if type(password) is not str:
        raise TypeError
    
    if len(password) >= 8:
        length = True

    for char in password:
        if char.isupper():
            upper_case = True

        if char.islower():
            lower_case = True

        if char.isdigit():
            digit = True

        if char in string.punctuation:
            special_character = True
    
    if length == True and lower_case == True and upper_case == True and digit == True and special_character == True:
        results = True
    else:
        results = False
    
    return results


# Question 2
def password_strength(password: str) -> str:
    """
    STEP 2: Determine the strength of a given password and return it as a string.

    Criteria:
        - "Weak" if the password is less than 8 characters long.
        - "Moderate" if it has 8 or more characters but is missing one or more
          of the following: uppercase, lowercase, digit, or special character.
        - "Strong" if it meets all password validation rules from Question 1.

    TODO: Implement the function to return one of these three strings.
    """

    checker = validate_password(password)

    if checker == True:
        return "Strong"
    elif len(password) >= 8 and checker == False:
        return "Moderate"
    elif checker == False:
        return "Weak"
    
print(password_strength("WT2!a"))
print(validate_password("WT2!a"))
    

