def welcome_message(name):
  """Prints a personalized welcome message.

  Args:
    name: The name of the person to welcome.
  """
  print(f"Welcome, {name}! We're so glad you joined us.")

def age_check(age):
  if age < 21:
    print("Unfortunately, you are still young")
  else:
    print("Welcome to the club brother!")  

# Get the user's name
user_name = input("Enter your name: ")
age = int(input("Enter your age:"))

# Call the function to print the welcome message
welcome_message(user_name)
age_check(age)