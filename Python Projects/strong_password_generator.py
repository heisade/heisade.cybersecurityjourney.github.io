import random
import string


def generated_password():
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ''.join(random.choices(characters, k = 12))
    return password

print(f'Generated password: {generated_password()}')