import random
import time
from colorama import Fore, Style

# Define Custom Coral Color
CORAL = "\033[38;2;255;127;80m"  
RESET = "\033[0m" 

# Welcome Message
print(Fore.CYAN + "\nWelcome, space traveler, to the wacky and wonderful universe of")
print("\"Galactic Giggles: A Space-Themed Mad Libs Adventure\"!")
time.sleep(1)

print("\nBefore we embark on this interstellar journey of chuckles and chaos,")
print("we need to know what to call the brave soul who dares to navigate the cosmos of comedy with us.")
time.sleep(1)

# Prompt User for Name
user_name = input("\nSo, what's your name, intrepid explorer? " + Style.RESET_ALL).capitalize()

# Prompt User to Roll the Die
print()
print(Fore.MAGENTA + "Ah, " + Fore.YELLOW + user_name + Fore.MAGENTA + ", a name that will surely be remembered in the history of space hilarity!")
time.sleep(1)

print("\nNow, to determine your fate in this galactic expedition,")
print("you won't just be rocketing blindly into the void...")
time.sleep(1)

print("\nOh no! You'll be rolling the ancient and mystical Cosmic Cube - a dice to you earthlings - ")
print("to decide which starry story you'll dive into.")
time.sleep(1)

print("\nWill it be a tale of alien encounters or a saga of space station shenanigans?")
time.sleep(1)

print("\nOnly the Cosmic Cube knows!")
time.sleep(1)

print("\nSo, give it a roll!")
time.sleep(1)

user_input = input("\nJust type 'roll' and let fate (with a little push from gravity) guide your adventure. " + Style.RESET_ALL) 

# Library of Dice Art
dice_art = {
    1: ("┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"),
    2: ("┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),
    3: ("┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"),
    4: ("┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"),
    5: ("┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"),
    6: ("┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘"),
}

# Library of Available Stories
stories = {
    1: "A Stellar Discovery",
    2: "The Galactic Chef Competition",
    3: "The Escape from The Moon of Dread",
    4: "The Space Opera",
    5: "The Intergalactic Marathon",
    6: "The Mystery of The Vanishing Satellites",
}

# Function to Print Dice Art
def print_dice_art(number):
    if number in dice_art:
        for line in dice_art[number]:
            print(line)
    else:
        print("Invalid")

# Main Gameplay Loop
while True:

    # Check if the User Input is "Roll"
    if user_input.lower() == "roll":

        # Function to Return a Random Number (between 1 and the number of sides on the die)
        def roll_dice(num):
            return random.randint(1, num)

        # Run Function and Store Result
        dice_result = roll_dice(6)
        print()
        print(Fore.CYAN + "Fantastic! The Cosmic Cube has spoken!\n" + Fore.YELLOW)
        time.sleep(1)

        # Print the Dice Art
        print_dice_art(dice_result)
        time.sleep(1)

        print()
        print(Fore.CYAN + "You rolled a " + str(dice_result) + ", propelling you into the adventure of " + stories[dice_result] + "!" + Fore.CYAN)
        time.sleep(1)

        # Story 1: A Stellar Discovery
        if dice_result == 1:

            # Function for Story 1
            def story_1():

                adjective = input("Choose an adjective: " + Style.RESET_ALL).capitalize()
                noun = input(Fore.CYAN + "Choose a plural-noun: " + Style.RESET_ALL).lower()
                made_up = input(Fore.CYAN + "Choose a made-up-place: " + Style.RESET_ALL).capitalize()
                adjective2 = input(Fore.CYAN + "Choose another adjective: " + Style.RESET_ALL).lower()
                name = input(Fore.CYAN + "Choose a name: " + Style.RESET_ALL).capitalize()
                noun2 = input(Fore.CYAN + "Choose another noun: " + Style.RESET_ALL).lower()
                noun3 = input(Fore.CYAN + "And again, choose another noun: " + Style.RESET_ALL).lower()

                print()
                print(Fore.MAGENTA + "A STELLAR DISCOVERY")
                time.sleep(1)
                print("During a routine scan of the cosmos,")
                time.sleep(1)
                print("astronomers at 'The " + Fore.YELLOW + adjective + Fore.MAGENTA + " Observatory' stumbled upon an unprecedented discovery:")
                time.sleep(1)
                print("a planet made entirely of " + Fore.YELLOW + noun + Fore.MAGENTA + ".")
                time.sleep(1)
                print("This planet, which they named '" + Fore.YELLOW + made_up + Fore.MAGENTA + "',")
                time.sleep(1)
                print("orbits a(n) " + adjective2 + " star in the '" + Fore.YELLOW + name + Fore.MAGENTA + " Galaxy'.")
                time.sleep(1)
                print("Not only is this planet unique for its composition,")
                time.sleep(1)
                print("but it also has rivers of liquid " + Fore.YELLOW + noun2 + Fore.MAGENTA + " and clouds of " + Fore.YELLOW + noun3 + Fore.MAGENTA + ",")
                time.sleep(1)
                print("making scientists rethink what is possible in the universe.")
                time.sleep(2)

            # Run Story 1 Function
            print()
            story_1()
            print()

            print(CORAL + "Ah, it appears the cosmos crave a bit more drama from us, " + Fore.YELLOW + user_name + CORAL +"!")
            time.sleep(1)

            print("\nThe Quantum Quasar Quibbler is humming with anticipation,")
            print("or it could just be that leftover space pizza from last night.")
            time.sleep(1)

            print("\nEither way, it's clear: ")
            print("fate demands a second roll to truly align the stars of storytelling and silliness.")
            time.sleep(1)

            user_input = input("\nType 'roll' to continue or 'quit' to exit: " + RESET)

        # Story 2: The Galactic Chef Competition
        elif dice_result == 2:

            # Function for Story 2
            def story_2():

                planet = input("Choose a planet: " + Style.RESET_ALL).capitalize()
                noun = input(Fore.CYAN + "Choose a plural-noun: " + Style.RESET_ALL).lower()
                noun2 = input(Fore.CYAN + "Choose another plural-noun: " + Style.RESET_ALL).lower()
                adjective = input(Fore.CYAN + "Choose an adjective: " + Style.RESET_ALL).lower()
                noun3 = input(Fore.CYAN + "And again, choose another plural-noun: " + Style.RESET_ALL).lower()
                verb_ing = input(Fore.CYAN + "Choose a verb ending in -ing: " + Style.RESET_ALL).lower()
                noun4 = input(Fore.CYAN + "Now, choose a noun: " + Style.RESET_ALL).lower()

                print()
                print(Fore.MAGENTA + "THE GALACTIC CHEF COMPETITION")
                time.sleep(1)
                print("In a galaxy not too far away,")
                time.sleep(1)
                print("the annual 'Galactic Chef Competition' was heating up.")    
                time.sleep(1)  
                print("Contestants from various planets gathered on " + Fore.YELLOW + planet + Fore.MAGENTA + ", ")
                time.sleep(1)
                print("each tasked with creating a dish that encapsulates the flavors of their home world")
                time.sleep(1)
                print("using only three ingredients: ")
                time.sleep(1)
                print(Fore.YELLOW + noun + Fore.MAGENTA + ", " + Fore.YELLOW + noun2 + Fore.MAGENTA + ", and " + Fore.YELLOW + adjective + Fore.MAGENTA + " " + Fore.YELLOW + noun3 + Fore.MAGENTA + ".")
                time.sleep(1)
                print("The catch? They had to cook in zero gravity,")
                time.sleep(1)
                print("making even the simple act of " + Fore.YELLOW + verb_ing + Fore.MAGENTA + " their ingredients a challenge.")
                time.sleep(1)
                print("The winner would earn the coveted title of 'Master Galactic Chef' and a trophy made of pure " + Fore.YELLOW + noun4 + Fore.MAGENTA + ".")
                time.sleep(2)

            # Run Story 2 Function
            print()
            story_2()
            print()

            print(CORAL + "In the infinite expanse of space, where time loops and gravity does the tango, ")
            print("your destiny awaits another turn of the Quantum Quasar Quibbler. ")
            time.sleep(1)

            print("\nWill it be a meteoric rise to fame or a black hole belly-flop? ")
            time.sleep(1)

            print("\nOnly one way to find out! ")
            time.sleep(1)

            print("\nLet's roll again and ride the wave of cosmic uncertainty to our next adventure!")
            time.sleep(1)

            user_input = input("\nType 'roll' to continue or 'quit' to exit: " + RESET)

        # Story 3: The Escape from the Moon of Dread
        elif dice_result == 3:

            # Function for Story 3
            def story_3():

                name = input("Choose a name: " + Style.RESET_ALL).capitalize()
                adjective = input(Fore.CYAN + "Choose an adjective: " + Style.RESET_ALL).lower()
                noun = input(Fore.CYAN + "Choose a noun: " + Style.RESET_ALL).lower()
                adjective2 = input(Fore.CYAN + "Choose another adjective: " + Style.RESET_ALL).lower()
                noun2 = input(Fore.CYAN + "Choose another noun: " + Style.RESET_ALL).lower()
                number = input(Fore.CYAN + "Choose a number: " + Style.RESET_ALL).lower()
                noun3 = input(Fore.CYAN + "Choose a plural-noun: " + Style.RESET_ALL).lower()
                noun4 = input(Fore.CYAN + "Choose another plural-noun: " + Style.RESET_ALL).lower()
                verb = input(Fore.CYAN + "Choose a verb: " + Style.RESET_ALL).lower()

                print()
                print(Fore.MAGENTA + "THE ESCAPE FROM THE MOON OF DREAD")
                time.sleep(1)
                print("After crash-landing on the notorious Moon of Dread,")
                time.sleep(1)
                print("the crew of the spaceship " + Fore.YELLOW + name + Fore.MAGENTA + " found themselves in a dire situation.")
                time.sleep(1)
                print("Surrounded by " + Fore.YELLOW + adjective + Fore.MAGENTA + " terrain and the constant threat of " + Fore.YELLOW + noun + Fore.MAGENTA + "-eating aliens,")
                time.sleep(1)
                print("they had to come up with a plan to escape.")
                time.sleep(1)
                print("Their only hope was to repair their ship's " + Fore.YELLOW + adjective2 + Fore.MAGENTA + " engine using spare parts from their cargo:")
                time.sleep(1)
                print("a(n) " + Fore.YELLOW + noun2 + Fore.MAGENTA + ", " + Fore.YELLOW + number + Fore.MAGENTA + " " + Fore.YELLOW + noun3 + Fore.MAGENTA + ", and the last of their " + noun4 + ".")
                time.sleep(1)
                print("Working against time,")
                time.sleep(1)
                print("they had to " + Fore.YELLOW + verb + Fore.MAGENTA + " together to avoid becoming the next meal for the moon's infamous inhabitants.")
                time.sleep(2)

            # Run Story 3 Function
            print()
            story_3()
            print()

            print(CORAL + "The interstellar odds are in your favor, or so the Martian bookkeepers tell me. ")
            time.sleep(1)

            print("\nBut fortune, like a cosmic comet, needs a little encouragement to swing by our little corner of space. ")
            time.sleep(1)

            print("\nReady to tempt the fates once more, " + Fore.YELLOW + user_name + CORAL + "? ")
            time.sleep(1)

            print("\nRoll again, and let's see if we can't win the galaxy's favor — or at least a smile from a passing asteroid.")
            time.sleep(1)

            user_input = input("\nType 'roll' to continue or 'quit' to exit: " + RESET)

        # Story 4: The Space Opera
        elif dice_result == 4:

            # Function for Story 4
            def story_4():

                print()
                adjective = input("Choose an adjective: " + Style.RESET_ALL).capitalize()
                adjective2 = input(Fore.CYAN + "Choose another adjective: " + Style.RESET_ALL).lower()
                name = input(Fore.CYAN + "Choose a name: " + Style.RESET_ALL).capitalize()
                adjective3 = input(Fore.CYAN + "And again, choose another adjective: " + Style.RESET_ALL).lower()
                noun = input(Fore.CYAN + "Choose a noun: " + Style.RESET_ALL).lower()
                adjective4 = input(Fore.CYAN + "And again, choose another adjective: " + Style.RESET_ALL).lower()
                noun2 = input(Fore.CYAN + "Choose another noun: " + Style.RESET_ALL).lower()
                adjective5 = input(Fore.CYAN + "One last time, choose another adjective: " + Style.RESET_ALL).lower()
                noun3 = input(Fore.CYAN + "And again, choose another noun: " + Style.RESET_ALL).capitalize()

                print()
                print(Fore.MAGENTA + "THE SPACE OPERA")
                time.sleep(1)
                print("In the grand tradition of intergalactic storytelling,")
                time.sleep(1)
                print("the space opera, 'The " + Fore.YELLOW + adjective + Fore.MAGENTA + " Nebula', premiered to an audience of thousands from across the universe.")
                time.sleep(1)
                print("The story follows the journey of a(n) " + Fore.YELLOW + adjective2 + Fore.MAGENTA + " hero, Captain " + Fore.YELLOW + name + Fore.MAGENTA + ", ")
                time.sleep(1)
                print("as they navigate through the " + Fore.YELLOW + adjective3 + Fore.MAGENTA + " nebula")
                time.sleep(1)
                print("to uncover the truth behind the mysterious disappearance of the " + Fore.YELLOW + noun + Fore.MAGENTA + ". ")
                time.sleep(1)
                print("Alongside a crew of misfits — a(n) " + Fore.YELLOW + adjective4 + Fore.MAGENTA + " scientist, a robotic " + Fore.YELLOW + noun2 + Fore.MAGENTA + " with a passion for poetry,")
                time.sleep(1)
                print("and a runaway alien princess — they face challenges like space pirates, a black hole, and their own " + Fore.YELLOW + adjective5 + Fore.MAGENTA + " pasts.")
                time.sleep(1)
                print("With a soundtrack performed by the renowned '" + Fore.YELLOW + noun3 + Fore.MAGENTA + " Orchestra',")
                time.sleep(1)
                print("it's a tale of adventure, love, and the search for identity among the stars.")
                time.sleep(2)

            # Run Story 4 Function
            print()
            story_4()
            print()

            print(CORAL + "Ah, it seems the cosmos are itching for another spin! ")
            time.sleep(1)

            print("\nThe stars are aligning, the planets are in position, ")
            print("and the black holes are... well, let's not worry about them right now. ")
            time.sleep(1)

            print("\nIt's your turn, " + Fore.YELLOW + user_name + CORAL + ", to stir the celestial pot of soup. ")
            time.sleep(1)

            print("\nGive us another roll, and let's see if we can make the universe dance to our tune!")
            time.sleep(1)

            user_input = input("\nType 'roll' to continue or 'quit' to exit: " + RESET)

        # Story 5: The Intergalactic Marathon
        elif dice_result == 5:

            # Function for Story 5
            def story_5():

                adjective = input("Choose an adjective: " + Style.RESET_ALL).lower()
                number = input(Fore.CYAN + "Choose a number: " + Style.RESET_ALL).lower()
                verb = input(Fore.CYAN + "Choose a verb: " + Style.RESET_ALL).lower()
                number2 = input(Fore.CYAN + "Choose another number: " + Style.RESET_ALL).lower()
                adjective2 = input(Fore.CYAN + "Choose another adjective: " + Style.RESET_ALL).lower()
                noun = input(Fore.CYAN + "Choose a plural-noun: " + Style.RESET_ALL).lower()
                name = input(Fore.CYAN + "Choose a name: " + Style.RESET_ALL).capitalize()
                noun2 = input(Fore.CYAN + "Choose a noun: " + Style.RESET_ALL).lower()
                planet = input(Fore.CYAN + "Choose a planet: " + Style.RESET_ALL).capitalize()
                adjective3 = input(Fore.CYAN + "And again, choose another adjective: " + Style.RESET_ALL).lower()

                print()
                print(Fore.MAGENTA + "THE INTERGALACTIC MARATHON")
                time.sleep(1)
                print("On a planet known for its " + Fore.YELLOW + adjective + Fore.MAGENTA + " landscapes and gravity that is " + Fore.YELLOW + number + Fore.MAGENTA + " times that of Earth's,")
                time.sleep(1)
                print("the Intergalactic Marathon is no small feat. ")
                time.sleep(1)
                print("Participants must run, jump, and " + Fore.YELLOW + verb + Fore.MAGENTA + " their way through a " + Fore.YELLOW + number2 + Fore.MAGENTA + "-mile course that includes")
                time.sleep(1)
                print("floating islands, " + Fore.YELLOW + adjective2 + Fore.MAGENTA + " valleys, and a river of " + Fore.YELLOW + noun + Fore.MAGENTA + ".")
                time.sleep(1)
                print("This year's favorite to win is " + Fore.YELLOW + name + Fore.MAGENTA + ",")
                time.sleep(1)
                print("a(n) " + Fore.YELLOW + noun2 + Fore.MAGENTA + " from the planet " + Fore.YELLOW + planet + Fore.MAGENTA + ",")
                time.sleep(1)
                print("known for their incredible speed and endurance.")
                time.sleep(1)
                print("Spectators from across the galaxy gather,")
                time.sleep(1)
                print("wearing " + Fore.YELLOW + adjective3 + Fore.MAGENTA + " hats and waving flags representing their home planets,")
                time.sleep(1)
                print("to cheer on the competitors.")
                time.sleep(2)

            # Run Story 5 Function
            print()
            story_5()
            print()

            print(Fore.YELLOW + user_name + CORAL +", let's not keep the universe waiting (it's got a tight schedule, after all). ")
            time.sleep(1)

            print("\nChannel your inner cosmic energy, ")
            print("whisper a sweet nothing to the Quantum Quasar Quibbler, ")
            print("and let's roll again! ")
            time.sleep(1)

            print("\nRemember, in space, no one can see you re-roll... ")
            print("unless it's broad-casted across the Galactic Network, but no pressure. ")
            time.sleep(1)

            user_input = input("\nType 'roll' to continue or 'quit' to exit: " + RESET)

        # Story 6: The Mystery of the Vanishing Satellites
        elif dice_result == 6:

            # Function for Story 6
            def story_6():

                name = input("Choose a name: " + Style.RESET_ALL).capitalize()
                planet = input(Fore.CYAN + "Choose a planet: " + Style.RESET_ALL).capitalize()
                name2 = input(Fore.CYAN + "Choose another name: " + Style.RESET_ALL).capitalize()
                adjective = input(Fore.CYAN + "Choose an adjective: " + Style.RESET_ALL).lower()
                adjective2 = input(Fore.CYAN + "Choose another adjective: " + Style.RESET_ALL).lower()
                name3 = input(Fore.CYAN + "And again, choose another name: " + Style.RESET_ALL).capitalize()
                noun = input(Fore.CYAN + "Choose a noun: " + Style.RESET_ALL).lower()
                noun2 = input(Fore.CYAN + "Choose another noun: "+ Style.RESET_ALL).lower()
                noun3 = input(Fore.CYAN + "And again, choose another noun: " + Style.RESET_ALL).lower()
                verb = input(Fore.CYAN + "Choose a verb: " + Style.RESET_ALL).lower()

                print()
                print(Fore.MAGENTA + "THE MYSTERY OF THE VANISHING SATELLITES")
                time.sleep(1)
                print("The space agency '" + Fore.YELLOW + name + Fore.MAGENTA + "' faced a puzzling crisis: ")
                time.sleep(1)
                print("their satellites around " + Fore.YELLOW + planet + Fore.MAGENTA + " were vanishing without a trace. ")
                time.sleep(1)
                print("Leading the investigation was Dr. " + Fore.YELLOW + name2 + Fore.MAGENTA + ", ")
                time.sleep(1)
                print("a(n) " + Fore.YELLOW + adjective + Fore.MAGENTA + " scientist known for solving the most baffling space mysteries.")
                time.sleep(1)
                print("The only clue was a series of " + Fore.YELLOW + adjective2 + Fore.MAGENTA + " signals intercepted moments before each disappearance.")
                time.sleep(1)
                print("Believing these signals to be key,")
                time.sleep(1)
                print("Dr. " + Fore.YELLOW + name2 + Fore.MAGENTA + " and their team embarked on a daring mission aboard the spacecraft '" + Fore.YELLOW + name3 + Fore.MAGENTA + "',")
                time.sleep(1)
                print("equipped with a(n) " + Fore.YELLOW + noun + Fore.MAGENTA + " and a(n) " + Fore.YELLOW + noun2 + Fore.MAGENTA + ", to unravel the mystery.")
                time.sleep(1)
                print("What they discovered was a hidden " + Fore.YELLOW + noun3 + Fore.MAGENTA + " with the power to " + verb + " matter,")
                time.sleep(1)
                print("guarded by an ancient alien civilization.")
                time.sleep(2)

            # Run Story 6 Function  
            print()
            story_6()
            print()

            print(CORAL + "Type roll once more, and let's catapult into our comedic cosmos ")
            print("with the grace of a gazelle galloping through gravity. ")
            time.sleep(1)

            print("\nWho knows, " + Fore.YELLOW + user_name + CORAL + "? This roll might just be the one that writes us into the annals of astral hilarity!")
            time.sleep(1)
            
            user_input = input("\nType 'roll' to continue or 'quit' to exit: " + RESET)

        # Error Message
        else:
            print(Fore.RED + "Invalid")

    # Quit Program and "Roll the Credits"
    elif user_input.lower() == "quit":
        print(Fore.CYAN + "\nRoll the credits!")  
        print("\nCreated by: Natasha Renee ♥")
        print("Tested By: Silas Reece ♫")
        print()
        break

    # Wrong Input for "Roll"
    else:
        print()
        print(CORAL + "Ah, attempting to communicate with the celestial beings using \"" + Fore.YELLOW + user_input + CORAL + "\".\n")
        time.sleep(1)
        print("A bold strategy!\n")
        time.sleep(1)
        print("Unfortunately, the intergalactic translators are currently tuned to 'dice' frequencies.\n")
        time.sleep(1)
        print("Try 'roll' to ensure we don't accidentally send a love poem to a black hole.")
        user_input = input("They're known to be quite clingy. " + Style.RESET_ALL)