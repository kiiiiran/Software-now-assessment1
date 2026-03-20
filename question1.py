# Ask user to enter password
password = input("Enter your password: ")

# Check conditions
length = len(password)
has_digit = False
has_upper = False

# Check each character
for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

# Determine strength
if length < 6:
    print("Weak password")
elif 6 <= length <= 10 and has_digit:
    print("Medium password")
elif length > 10 and has_digit and has_upper:
    print("Strong password")
else:
    print("Weak password")