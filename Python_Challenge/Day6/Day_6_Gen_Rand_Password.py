# Day_6 : Generate a random 8 characters password
import random
import string

# Define the character pool.
characters = string.ascii_letters + string.digits + string.punctuation

# Randomly choose 8 characters for password
password = ''.join(random.choices(characters, k=8))

print("Generated Password: ", password)