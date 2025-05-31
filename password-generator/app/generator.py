import random
import string

def generate_password(length, use_digits, use_symbols, use_uppercase, use_lowercase):
    if length < 1:
        raise ValueError("Password length must be at least 1")

    char_sets = []
    required_chars = []

    if use_digits:
        char_sets.append(string.digits)
        required_chars.append(random.choice(string.digits))
    if use_symbols:
        char_sets.append(string.punctuation)
        required_chars.append(random.choice(string.punctuation))
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
        required_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
        required_chars.append(random.choice(string.ascii_lowercase))

    if not char_sets:
        raise ValueError("At least one character type must be selected")

    all_chars = ''.join(char_sets)
    remaining_length = length - len(required_chars)

    password = required_chars + random.choices(all_chars, k=remaining_length)
    random.shuffle(password)

    return ''.join(password)