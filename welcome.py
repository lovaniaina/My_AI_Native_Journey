def welcome_message(name):
  """Prints a personalized welcome message.

  Args:
    name: The name of the person to welcome.
  """
  print(f"Welcome, {name}! We're so glad you joined us.")
user_name = input("Enter your name: ")
welcome_message(user_name)

def age_check(age):
  if age < 21:
    print("Unfortunately, you are still young")
  else:
    print("Welcome to the club brother!")  

# Get the user's name
age = int(input("Enter your age:"))

# Call the function to print the welcome message
age_check(age)