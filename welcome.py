def welcome_message(name):
  """Prints a personalized welcome message.

  Args:
    name: The name of the person to welcome.
  """
  # Set the actual special name (you can change "john" to your name)
  special_name = "john"

  # Convert the entered name to lowercase for a case-insensitive check
  if name.lower() == special_name:
    print(f"Welcome back, {name}! It's great to see you again, special friend!")
  else:
    # If the name is not the special name, print a regular welcome
    print(f"Welcome, {name}! Unfortunately, you entered a wrong name. Please try again.")


# Get the user's name
user_name = input("Enter your name: ")

# Call the function to display the appropriate message
welcome_message(user_name)