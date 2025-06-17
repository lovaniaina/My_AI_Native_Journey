# Welcome to your secret clubhouse login!

# First, let's set our secret username and password.
# These are like the "correct" keys to get into our clubhouse.
secret_username = "soccer_star"
secret_password = "goal!"

print("--- Welcome to the Secret Soccer Clubhouse! ---")

# Ask the user for their username
entered_username = input("Enter your username: ")

# Ask the user for their password
entered_password = input("Enter your password: ")

# Now, let's check if the entered username and password are correct using if/else!
if entered_username == secret_username and entered_password == secret_password:
    # This block runs ONLY if BOTH the username AND the password are correct
    print("------------------------------------------")
    print("Access Granted! Welcome, Soccer Star! You're in!")
    print("------------------------------------------")
else:
    # This block runs if EITHER the username OR the password (or both) are wrong
    print("------------------------------------------")
    print("Access Denied! Incorrect username or password. Try again!")
    print("------------------------------------------")

print("Thanks for trying to log in!")