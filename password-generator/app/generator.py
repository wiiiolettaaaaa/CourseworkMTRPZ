import string
import random

def generate_password(length=12, digits=True, symbols=True, uppercase=True):
    characters = []

    if digits:
        characters += list(string.digits)
    if symbols:
        characters += list("!@#$%^&*()")
    if uppercase:
        characters += list(string.ascii_uppercase)

    if not characters:
        raise ValueError("No character sets selected.")

    characters += list(string.ascii_lowercase)

    return ''.join(random.choice(characters) for _ in range(length))