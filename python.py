import random
import string
def generating_password(length,strength):
    if(strength=="weak"):
        chars=string.ascii_lowercase
    elif(strength=="medium"):
        chars=string.ascii_letters
    elif(strength=="strong"):
        chars=string.ascii_letters+string.digits+string.punctuation
    else:
        return "Invalid"
    password_chars = []
    for _ in range(length):
        password_chars.append(random.choice(chars))
    password = ''.join(password_chars)
    return password
length=int(input("enter the password length:"))
strength=input("enter strength of password:").lower()
print(generating_password(length,strength))          