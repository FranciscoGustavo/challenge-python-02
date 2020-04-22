# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
LOWERCASE_ABC = list('abcdefghijklmnopqrstvwxyz')
UPPERCASE_ABC = list('ABCDEFGHIJKLMNOPQRSTvWXYZ')
NUMBERS = list('0123456789')
TYPE = ['SYMBOLS', 'LOWERCASE', 'UPPERCASE', 'NUMBERS']

def generate_password():
    password_len = random.randint(8, 16)
    secure_pass = ''
    for idx in range(password_len):
        type_char = random.choice(TYPE)
        if type_char == 'SYMBOLS':
            secure_pass += random.choice(SYMBOLS)
        elif type_char == 'LOWERCASE':
            secure_pass += random.choice(LOWERCASE_ABC)
        elif type_char == 'UPPERCASE':
            secure_pass += random.choice(UPPERCASE_ABC)
        elif type_char == 'NUMBERS':
            secure_pass += random.choice(NUMBERS)

    if not validate(secure_pass):
        return generate_password()
        
    return secure_pass


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
