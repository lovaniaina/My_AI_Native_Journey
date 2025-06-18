# --- Simple Login System with Username and Passcode ---

# First, let's allow the user to CREATE their username and passcode.
print("------------------------------------------")
print("Welcome to the Account Creation System!")
print("------------------------------------------")

# 1. Ask the user to create their SECRET username
SECRET_USERNAME = input("Please create your desired username: ")

# 2. Ask the user to create their SECRET passcode
SECRET_PASSCODE = input("Please create your desired passcode: ")

print("\nGreat! Your account has been created.")
print("Now, let's try logging in with your new credentials.")
print("------------------------------------------")
print("Welcome to the Secure Game Login!")
print("------------------------------------------")

# Now, we ask the user to ENTER the credentials they just created for login.

# 3. Ask the user for their username for login
entered_username = input("Please enter your username to log in: ")

# 4. Ask the user for their passcode for login
entered_passcode = input("Please enter your passcode to log in: ")

# 5. Use an if/else statement to check BOTH conditions at once
#    We use 'and' to make sure BOTH the username AND the passcode are correct.
if entered_username == SECRET_USERNAME and entered_passcode == SECRET_PASSCODE:
    # This block runs ONLY if both conditions are TRUE
    print("\n------------------------------------------")
    print(f"Access GRANTED! Welcome, {entered_username}! Get ready to play! 🎉")
    print("------------------------------------------")
else:
    # This block runs if the 'if' condition is FALSE.
    # This means EITHER the username was wrong, OR the passcode was wrong, OR both were wrong.
    print("\n------------------------------------------")
    print("Access DENIED! Incorrect username or passcode. Please try again.")
    print("------------------------------------------")

print("\nThank you for attempting to log in!")
