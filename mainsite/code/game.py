import random
import string

def generate_passkeys():
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(10))
    return random_string


if __name__ == '__main__':
    print(generate_passkeys())