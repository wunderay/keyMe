import hashlib, secrets, string
def master_password(user_password:str):
    salt = secrets.token_bytes(64)
    password = hashlib.pbkdf2_hmac("sha512", user_password.encode("UTF-8"), salt, 100000, 32)
    print(password)


def generate_password(invalid_char="", option=3, length=12):
    """
    Generates a secure random password
    :param invalid_char: string of special characters that won't be used in the password
    :param option: Generates password with [0] lowercase letters only
                    [1] lowercase letters and numbers
                    [2] lower and upper case letters and numbers
                    [3] lower and upper case letters, numbers, and special characters
                    (Default is 3)
    :param length: output length of the password (Default is 12)
    :return: password as string object 
    """
    alphabet = string.ascii_lowercase
    if option == 0:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
    if option > 0:
        alphabet += string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if any(c.islower() for c in password) and sum(c.isdigit() for c in password) >= 1:
                break
    if option > 1:
        alphabet += string.ascii_uppercase
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 1):
                break
    if option == 3:
        punctuation = string.punctuation
        for c in invalid_char:
            punctuation = punctuation.replace(c, "")
        alphabet += punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 1)\
                    and any(c in string.punctuation for c in password):
                break
    return password


key = generate_password(invalid_char='* = " ; . | < > &'.strip(" "), option=3)
print(key)
