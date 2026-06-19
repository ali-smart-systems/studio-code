
import random
import string

def generate_password():
    length = random.randint(10, 10)

    password_type = random.choice(["letters", "digits", "symbols", "mix"])

    if password_type == "letters":
        chars = string.ascii_letters
    elif password_type == "digits":
        chars = string.digits
    elif password_type == "symbols":
        chars = string.punctuation
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password


print("Generated Password:", generate_password())