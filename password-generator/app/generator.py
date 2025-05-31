import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True, use_uppercase=True, use_lowercase=True):
    characters = ''
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase

    if not characters:
        raise ValueError("No character types selected")

    return ''.join(random.choice(characters) for _ in range(length))