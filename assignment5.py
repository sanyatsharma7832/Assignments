import re

password = input("Enter password: ")

if (len(password) >= 8 and
    re.search(r'[a-z]', password) and
    re.search(r'[A-Z]', password) and
    re.search(r'[0-9]', password) and
    re.search(r'[^a-zA-Z0-9]', password)):

    print("Password is strong")
else:
    print("Password is weak")