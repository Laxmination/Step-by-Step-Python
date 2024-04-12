# Random password Generator
import random
import string
pw_len = 8
charvalues = string.ascii_letters + string.digits + string.punctuation

# password = "".join([random.choice(charvalues) for i in range(pw_len)])                    # list comprehension [function for i in range(n)]
password = ""
for i in range(pw_len):
    password += random.choice(charvalues)

print("Your random password is:", password)