import re

def is_valid_gmail_id(email):
    pattern = r'^[A-Za-z0-9._%+-]+@gmail\.com$'
    return bool(re.search(pattern,email))
email = input("Enter Gmail ID: ")

if is_valid_gmail_id(email):
    print("Valid Gmail ID.")
else:
    print("Invalid Gmail ID.")





