import re
import math
import time
def password_strength(password):
    length_criteria = len(password) >= 8
    complexity_criteria = any(c.islower() for c in password) and \
                          any(c.isupper() for c in password) and \
                          any(c.isdigit() for c in password) and \
                          any(not c.isalnum() for c in password)
    uniqueness_criteria = len(password) == len(set(password))
    char_set_size = 0
    if any(c.islower() for c in password):
        char_set_size += 26
    if any(c.isupper() for c in password):
        char_set_size += 26
    if any(c.isdigit() for c in password):
        char_set_size += 10
    if any(not c.isalnum() for c in password):
        char_set_size += 32 

    entropy = len(password) * math.log2(char_set_size)
    estimated_crack_time_seconds = 2 ** entropy / (10 ** 9) 
    if estimated_crack_time_seconds < 60:
        estimated_crack_time = f"{estimated_crack_time_seconds:.2f} seconds"
    elif estimated_crack_time_seconds < 3600:
        estimated_crack_time = f"{estimated_crack_time_seconds / 60:.2f} minutes"
    elif estimated_crack_time_seconds < 86400:
        estimated_crack_time = f"{estimated_crack_time_seconds / 3600:.2f} hours"
    else:
        estimated_crack_time = f"{estimated_crack_time_seconds / 86400:.2f} days"
    print(f"Password Length: {'Good' if length_criteria else 'Too Short'}")
    print(f"Complexity: {'Good' if complexity_criteria else 'Weak'}")
    print(f"Uniqueness: {'Unique' if uniqueness_criteria else 'Not Unique'}")
    print(f"Estimated Time to Crack: {estimated_crack_time}")
password = input("Enter a password to check: ")
password_strength(password)
