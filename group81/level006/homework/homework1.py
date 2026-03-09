correct_password = "goa"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input('Enter your password: ')
    if password == correct_password:
        print("Access granted")
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print("Incorrect password try again")
        else:
            print("You have reached the maximum number of attempts")