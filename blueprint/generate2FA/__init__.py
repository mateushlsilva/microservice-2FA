from random import choice
import string

def generate():
    characters = string.ascii_letters + string.digits
    gen2FA = ''.join(choice(characters.upper()) for i in range(8))
    print(gen2FA)