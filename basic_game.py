# Welcome, Adventurer! Let's play a simple text adventure game.
# This game uses only if/else statements to make decisions!

print("---------------------------------------")
print("Welcome to the Mysterious Forest Adventure!")
print("---------------------------------------")
print("You wake up in a strange forest. You don't remember how you got here.")
print("The trees are tall, and there's a faint path in front of you.")

# --- First Decision Point ---
print("\nYou see two paths ahead: one going LEFT and one going RIGHT.")
choice1 = input("Do you go LEFT or RIGHT? (type 'left' or 'right'): ").lower() # .lower() makes sure 'Left' or 'LEFT' work too!

if choice1 == "left":
    print("\nYou chose to go LEFT. The path is narrow and winds deeper into the trees.")
    print("After a while, you stumble upon a sparkling, clear river!")

    # --- Second Decision Point (if you went LEFT) ---
    print("\nThe river looks inviting. Do you FOLLOW the river downstream, or try to CROSS it?")
    choice2a = input("Type 'follow' or 'cross': ").lower()

    if choice2a == "follow":
        print("\nYou decided to FOLLOW the river. It leads you to a cozy little cabin with smoke coming from the chimney.")
        print("A kind old hermit welcomes you in for a warm meal. You're safe!")
        print("\n*** CONGRATULATIONS! You found a safe haven! YOU WIN! ***")
    else: # This 'else' covers anything other than 'follow', effectively meaning 'cross'
        print("\nYou decided to CROSS the river. The current is stronger than it looks!")
        print("You slip, hit your head, and wake up even more lost than before. Oh no!")
        print("\n*** GAME OVER! You got lost! ***")

else: # This 'else' covers anything other than 'left', effectively meaning 'right'
    print("\nYou chose to go RIGHT. The path seems darker and leads towards some ominous-looking rocks.")
    print("Soon, you find the entrance to a dark, cold CAVE.")

    # --- Second Decision Point (if you went RIGHT) ---
    print("\nThe cave looks spooky. Do you DARE enter the cave, or try to FIND another path around it?")
    choice2b = input("Type 'dare' or 'find': ").lower()

    if choice2b == "dare":
        print("\nYou bravely DARE to enter the cave. It's pitch black inside!")
        print("Suddenly, you hear a loud growl and feel huge paws chasing you. RUN!")
        print("\n*** GAME OVER! A monster got you! ***")
    else: # This 'else' covers anything other than 'dare', effectively meaning 'find'
        print("\nYou decided to FIND another path. You carefully navigate around the rocky entrance.")
        print("After some climbing, you emerge into a beautiful, sunny clearing with a road!")
        print("\n*** CONGRATULATIONS! You found your way out! YOU WIN! ***")

print("\nThanks for playing The Mysterious Forest Adventure!")