import re

def pass_validator(pw):

    # Strong: The password has to meet all the requirements.
    # atleast 8 char long, has atleast one uppercase lowercase and digit charater
    strong_pw = re.compile(r'''
    (?=.{8,})       # atleast 8 charactwer long
    (?=.*[a-z])     # small letter
    (?=.*[A-Z])     # capital letter
    (?=.*[0-9])     # digit
    ''', re.VERBOSE)


    # Medium: If the password is at least six characters long
    # and meets all the other requirements,
    # or has no digit but meets the rest of the requirements.
    medium_pw = re.compile(r'''
    ((?=.{6,})       # atleast 6 charactwer long
    (?=.*[a-z])      # small letter
    (?=.*[A-Z])      # capital letter
    (?=.*[0-9]))     # digit
    |
    ((?=.{8,})       # atleast 8 charactwer long
    (?=.*[a-z])      # small letter
    (?=.*[A-Z]))     # capital letter
    ''', re.VERBOSE)


    spwmat = strong_pw.search(pw)
    mpwmat = medium_pw.search(pw)


    if spwmat:
        return 'Your password strength is STRONG'
    elif mpwmat:
        return 'Your password strength is MEDIUM'
    else:
        return 'Your password strength is WEAK'



pw = str(input('Enter your password : '))
strength = pass_validator(pw)
print(strength)