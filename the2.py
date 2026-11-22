# WO3 PROJECT: TEXT BASED ADVENTURE GAME: The Mysterious Forest
# The game objective is to survive the mysterious forest by making the right decisions.Each choice you make determines what happens next. Choose wisely!
scenario = (
    "You are in a dark forest at night. You hear strange noises coming from the bushes. "
    "Fortunately you find 2 items on the ground. "
    "Which item do you want to pick up? Type MATCH to pick up the match or FLASHLIGHT to pick up the flashlight: "
)

choice = input(scenario).lower()

#  BRANCH 1: MATCH 
if choice == "match":
    print(
        "\nYou pick up the match and strike it, and for an instant, the forest around you is illuminated. "
        "You see a large grizzly bear, and then the match burns out."
    )
    bear_choice = input("Do you want to RUN or HIDE behind trees?: ").lower()

    # Nested if statement inside the "match" branch
    if bear_choice == "run":
        print("\nYou sprint blindly through the dark and trip over a root, alerting the bear. Game Over!")
    elif bear_choice == "hide":
        print("\nYou quietly slip behind a thick oak tree. The bear sniffs the air and walks away.")
        path_choice = input("Now that the coast is clear, do you FOLLOW the river or CLIMB a hill?: ").lower()
        
        # Second level of nesting
        if path_choice == "follow":
            print("\nYou follow the river downstream and find a ranger station. You survived!")
        elif path_choice == "climb":
            print("\nYou climb the hill, spot city lights in the distance, and walk to safety. You survived!")
        else:
            print("\nYou hesitated too long and got lost in the dark. Game Over!")
    else:
        print("\nInvalid choice. Frozen with fear, the bear finds you. Game Over!")

#  BRANCH 2: FLASHLIGHT ---
elif choice == "flashlight":
    print(
        "\nYou turn on the flashlight and see a path ahead. "
        "But the batteries are low and it might die soon."
    )
    light_choice = input("Do you want to WALK or STAY PUT?: ").lower()

    # Nested if statement inside the "flashlight" branch
    if light_choice == "walk":
        print("\nYou hurry down the path before the light fades and reach an abandoned cabin.")
        cabin_choice = input("Do you KNOCK on the door or LOOK through the window?: ").lower()
        
        # Second level of nesting
        if cabin_choice == "knock":
            print("\nA friendly hiker opens the door and lets you in until morning. You survived!")
        elif cabin_choice == "look":
            print("\nThe floorboards give way under you and you fall into a cellar. Game Over!")
        else:
            print("\nYour flashlight dies while you stand outside in the cold. Game Over!")
    elif light_choice == "stay put":
        print("\nYour flashlight flickers out, leaving you alone in the freezing woods until morning. Game Over!")
    else:
        print("\nInvalid choice. While deciding, your flashlight dies completely. Game Over!")

#  BRANCH 3: INVALID FIRST CHOICE
else:
    print("\nInvalid choice. Please restart and choose either 'match' or 'flashlight'.")
