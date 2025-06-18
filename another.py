def welcome_message(name):
  """Prints a personalized welcome message based on the name,
  and returns True if the name is recognized, False otherwise.

  Args:
    name: The name of the person to welcome.
  """
  # Define our special names
  super_special_name = "Lova"
  another_special_friend = "PythonBuddy" # Let's add another special name!

  # Check for the super special name first (case-insensitive)
  if name.upper() == super_special_name.upper():
    print(f"\nWelcome back, {name}! It's SO great to see you again, my very special friend! 🎉")
    return True # Name was correct, so we return True

  # Check for another special friend
  elif name.upper() == another_special_friend.upper():
    print(f"\nHello, {name}! Glad you're here, PythonBuddy! We've been waiting for you! �")
    return True # Name was correct, so we return True

  # If neither of the special names matched
  else:
    print(f"\nWelcome, {name}! Unfortunately, you entered an unrecognized name. Please try again.")
    return False # Name was incorrect, so we return False

# --- NEW: Function to understand the time input ---
def parse_time_input(time_string):
  """
  Attempts to convert a user's time input (like '9 am', '3 pm', '14')
  into a 24-hour format hour (0-23).
  Returns the hour as an integer, or -1 if the input isn't understood.
  """
  try:
    time_string = time_string.lower().strip() # Make it lowercase and remove extra spaces

    # Split the input, e.g., "3 pm" becomes ["3", "pm"]
    parts = time_string.split(' ')
    hour = int(parts[0]) # Try to get the number part first

    # Check if there's an 'am' or 'pm'
    if len(parts) > 1:
      ampm = parts[1]
      if ampm == 'pm' and hour != 12: # If it's PM and not 12 PM, add 12 to the hour
        hour += 12
      elif ampm == 'am' and hour == 12: # If it's 12 AM (midnight), make it 0 in 24-hour format
        hour = 0
    
    # Check if the hour is a valid time (0 to 23)
    if 0 <= hour <= 23:
      return hour # Return the valid hour
    else:
      return -1 # Return -1 to signal an invalid hour

  except (ValueError, IndexError):
    # If something goes wrong (like typing "hello" instead of a number),
    # we return -1 to signal an error
    return -1

# --- Main part of the script ---

# This loop will keep asking for the name until a recognized one is entered
name_is_correct = False
while not name_is_correct:
    user_name = input("Enter your name: ")
    # The welcome_message function will tell us if the name was correct
    name_is_correct = welcome_message(user_name)

# After the loop, it means a correct name was entered.
# Now, let's ask about the time of day for another special greeting!
print("\nGreat! Now that you're logged in, let's make it even more welcoming.")

# --- Get and Parse Time of Day Input ---
parsed_hour = -1 # Start with an invalid hour
while parsed_hour == -1: # Keep asking until we get a valid time
    time_of_day_input = input("What time is it right now? (e.g., '9 am', '3 pm', '22', '14:00'): ")
    parsed_hour = parse_time_input(time_of_day_input)
    if parsed_hour == -1:
        print("Sorry, I couldn't understand that time. Please try again using formats like '9 am', '3 pm', or '14'.")

# --- Time of Day Greeting using if/elif/else based on numerical hour ---
if 5 <= parsed_hour <= 11:  # Morning: 5 AM to 11 AM
    print("Good morning! Time to start a new day of coding fun!")
elif 12 <= parsed_hour <= 17: # Afternoon: 12 PM to 5 PM
    print("Good afternoon! Hope you're having a productive day!")
elif 18 <= parsed_hour <= 23 or (0 <= parsed_hour <= 4): # Evening/Night: 6 PM to 11 PM OR 12 AM to 4 AM
    print("Good evening! Relax and enjoy your time!")
# An 'else' here is generally not needed if parse_time_input ensures valid range
# and all valid ranges are covered by the if/elif.

print("\nThanks for using our enhanced welcome system!")