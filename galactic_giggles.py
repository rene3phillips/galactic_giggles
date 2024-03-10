import random

print("Welcome, space traveler, to the wacky and wonderful universe of",
      "\"Galactic Giggles: A Space-Themed Mad Libs Adventure\"!",
      "Before we embark on this interstellar journey of chuckles and chaos,",
      "we need to know what to call the brave soul who dares to navigate the cosmos of comedy with us.",
      sep="\n")

user_name = input("So, what's your name, intrepid explorer? ").capitalize()

print()
print("Ah, " + user_name + ", a name that will surely be remembered in the history of space hilarity!",
      "Now, to determine your fate in this galactic expedition,",
      "you won't just be rocketing blindly into the void...",
      "Oh no! You'll be rolling the ancient and mystical Cosmic Cube - a dice to you earthlings - ",
      "to decide which starry story you'll dive into.",
      "Will it be a tale of alien encounters or a saga of space station shenanigans?",
      "Only the Cosmic Cube knows!",
      "So, give it a roll!",
      sep="\n")

# library - dice art
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

# library - stories
stories = {
    1: "A Stellar Discovery",
    2: "The Galactic Chef Competition",
    3: "The Escape from The Moon of Dread",
    4: "The Space Opera",
    5: "The Intergalactic Marathon",
    6: "The Mystery of The Vanishing Satellites",
}


def print_dice_art(number):
    if number in dice_art:
        for line in dice_art[number]:
            print(line)
    else:
        print("Invalid")


user_input = input("Just type 'roll' and let fate (with a little push from gravity) guide your adventure. ")

while True:
    if user_input.lower() == "roll":
        def roll_dice(num):
            return random.randint(1, num)


        dice_result = roll_dice(6)
        print()
        print("Fantastic! The Cosmic Cube has spoken!")
        print_dice_art(dice_result)
        print(
            "You rolled a " + str(dice_result) + ", propelling you into the adventure of " + stories[dice_result] + "!")

        if dice_result == 1:
            def story_1():
                adjective = input("Choose an adjective: ").capitalize()
                noun = input("Choose a plural-noun: ").lower()
                made_up = input("Choose a made-up-place: ").capitalize()
                adjective2 = input("Choose another adjective: ").lower()
                name = input("Choose a name: ").capitalize()
                noun2 = input("Choose another noun: ").lower()
                noun3 = input("And again, choose another noun: ").lower()
                print()
                print("A STELLAR DISCOVERY")
                print("During a routine scan of the cosmos,")
                print("astronomers at 'The " + adjective + " Observatory' stumbled upon an unprecedented discovery:")
                print("a planet made entirely of " + noun + ".")
                print("This planet, which they named '" + made_up + "',")
                print("orbits a(n) " + adjective2 + " star in the '" + name + " Galaxy'.")
                print("Not only is this planet unique for its composition,")
                print("but it also has rivers of liquid " + noun2 + " and clouds of " + noun3 + ",")
                print("making scientists rethink what is possible in the universe.")
            print()
            story_1()
            print()
            print("Ah, it appears the cosmos crave a bit more drama from us, " + user_name + "!",
                    "The Quantum Quasar Quibbler is humming with anticipation,",
                    "or it could just be that leftover space pizza from last night.",
                    "Either way, it's clear: ",
                    "fate demands a second roll to truly align the stars of storytelling and silliness.",
                    sep="\n")
            user_input = input("Type 'roll' to continue or 'quit' to exit: ")

        elif dice_result == 2:
            def story_2():
                planet = input("Choose a planet: ").capitalize()
                noun = input("Choose a plural-noun: ").lower()
                noun2 = input("Choose another plural-noun: ").lower()
                adjective = input("Choose an adjective: ").lower()
                noun3 = input("And again, choose another plural-noun: ").lower()
                verb_ing = input("Choose a verb ending in -ing: ").lower()
                noun4 = input("Now, choose a noun: ").lower()
                print()
                print("THE GALACTIC CHEF COMPETITION",
                      "In a galaxy not too far away,",
                      "the annual 'Galactic Chef Competition' was heating up.",
                      "Contestants from various planets gathered on " + planet + ", ",
                      "each tasked with creating a dish that encapsulates the flavors of their home world",
                      "using only three ingredients: ",
                      noun + ", " + noun2 + ", and " + adjective + " " + noun3 + ".",
                      "The catch? They had to cook in zero gravity,",
                      "making even the simple act of " + verb_ing + " their ingredients a challenge.",
                      "The winner would earn the coveted title of 'Master Galactic Chef' and a trophy made of pure " + noun4 + ".",
                      sep="\n")
            print()
            story_2()
            print()
            print("In the infinite expanse of space, where time loops and gravity does the tango, ",
                  "your destiny awaits another turn of the Quantum Quasar Quibbler. ",
                  "Will it be a meteoric rise to fame or a black hole belly-flop? ",
                  "Only one way to find out! ",
                  "Let's roll again and ride the wave of cosmic uncertainty to our next adventure!",
                  sep="\n")
            user_input = input("Type 'roll' to continue or 'quit' to exit: ")

        elif dice_result == 3:
            def story_3():
                name = input("Choose a name: ").capitalize()
                adjective = input("Choose an adjective: ").lower()
                noun = input("Choose a noun: ").lower()
                adjective2 = input("Choose another adjective: ").lower()
                noun2 = input("Choose another noun: ").lower()
                number = input("Choose a number: ").lower()
                noun3 = input("Choose a plural-noun: ").lower()
                noun4 = input("Choose another plural-noun: ").lower()
                verb = input("Choose a verb: ").lower()
                print()
                print("THE ESCAPE FROM THE MOON OF DREAD",
                      "After crash-landing on the notorious Moon of Dread,",
                      "the crew of the spaceship " + name + " found themselves in a dire situation.",
                      "Surrounded by " + adjective + " terrain and the constant threat of " + noun + "-eating aliens,",
                      "they had to come up with a plan to escape.",
                      "Their only hope was to repair their ship's " + adjective2 + " engine using spare parts from their cargo:",
                      "a(n) " + noun2 + ", " + number + " " + noun3 + ", and the last of their " + noun4 + ".",
                      "Working against time,",
                      "they had to " + verb + " together to avoid becoming the next meal for the moon's infamous inhabitants.",
                      sep="\n")
            print()
            story_3()
            print()
            print("The interstellar odds are in your favor, or so the Martian bookkeepers tell me. ",
                  "But fortune, like a cosmic comet, needs a little encouragement to swing by our little corner of space. ",
                  "Ready to tempt the fates once more, " + user_name + "? ",
                  "Roll again, and let's see if we can't win the galaxy's favor — or at least a smile from a passing asteroid.",
                  sep="\n")
            user_input = input("Type 'roll' to continue or 'quit' to exit: ")

        elif dice_result == 4:
            def story_4():
                print()
                adjective = input("Choose an adjective: ").capitalize()
                adjective2 = input("Choose another adjective: ").lower()
                name = input("Choose a name: ").capitalize()
                adjective3 = input("And again, choose another adjective: ").lower()
                noun = input("Choose a noun: ").lower()
                adjective4 = input("And again, choose another adjective: ").lower()
                noun2 = input("Choose another noun: ").lower()
                adjective5 = input("One last time, choose another adjective: ").lower()
                noun3 = input("And again, choose another noun: ").capitalize()
                print()
                print("THE SPACE OPERA",
                      "In the grand tradition of intergalactic storytelling,",
                      "the space opera, 'The " + adjective + " Nebula', premiered to an audience of thousands from across the universe.",
                      "The story follows the journey of a(n) " + adjective2 + " hero, Captain " + name + ", ",
                      "as they navigate through the " + adjective3 + " nebula",
                      "to uncover the truth behind the mysterious disappearance of the " + noun + ". ",
                      "Alongside a crew of misfits — a(n) " + adjective4 + " scientist, a robotic " + noun2 + " with a passion for poetry,",
                      "and a runaway alien princess — they face challenges like space pirates, a black hole, and their own " + adjective5 + " pasts.",
                      "With a soundtrack performed by the renowned '" + noun3 + " Orchestra',",
                      "it's a tale of adventure, love, and the search for identity among the stars.",
                      sep="\n")
                print()
            story_4()
            print("Ah, it seems the cosmos are itching for another spin! ",
                  "The stars are aligning, the planets are in position, ",
                  "and the black holes are... well, let's not worry about them right now. ",
                  "It's your turn, " + user_name + ", to stir the celestial pot of soup. ",
                  "Give us another roll, and let's see if we can make the universe dance to our tune!",
                  sep="\n")
            user_input = input("Type 'roll' to continue or 'quit' to exit: ")

        elif dice_result == 5:
            def story_5():
                adjective = input("Choose an adjective: ").lower()
                number = input("Choose a number: ").lower()
                verb = input("Choose a verb: ").lower()
                number2 = input("Choose another number: ").lower()
                adjective2 = input("Choose another adjective: ").lower()
                noun = input("Choose a plural-noun: ").lower()
                name = input("Choose a name: ").capitalize()
                noun2 = input("Choose a noun: ").lower()
                planet = input("Choose a planet: ").capitalize()
                adjective3 = input("And again, choose another adjective: ").lower()
                print()
                print(
                    "THE INTERGALACTIC MARATHON",
                    "On a planet known for its " + adjective + " landscapes and gravity that is " + number + " times that of Earth's,",
                    "the Intergalactic Marathon is no small feat. ",
                    "Participants must run, jump, and " + verb + " their way through a " + number2 + "-mile course that includes",
                    "floating islands, " + adjective2 + " valleys, and a river of " + noun + ".",
                    "This year's favorite to win is " + name + ",",
                    "a(n) " + noun2 + " from the planet " + planet + ",",
                    "known for their incredible speed and endurance.",
                    "Spectators from across the galaxy gather,",
                    "wearing " + adjective3 + " hats and waving flags representing their home planets,",
                    "to cheer on the competitors.",
                    sep="\n")
            print()
            story_5()
            print()
            print(user_name + ", let's not keep the universe waiting (it's got a tight schedule, after all). ",
                  "Channel your inner cosmic energy, ",
                  "whisper a sweet nothing to the Quantum Quasar Quibbler, ",
                  "and let's roll again! ",
                  "Remember, in space, no one can see you re-roll... ",
                  "unless it's broad-casted across the Galactic Network, but no pressure. ",
                  sep="\n")
            user_input = input("Type 'roll' to continue or 'quit' to exit: ")

        elif dice_result == 6:
            def story_6():
                name = input("Choose a name: ").capitalize()
                planet = input("Choose a planet: ").capitalize()
                name2 = input("Choose another name: ").capitalize()
                adjective = input("Choose an adjective: ").lower()
                adjective2 = input("Choose another adjective: ").lower()
                name3 = input("And again, choose another name: ").capitalize()
                noun = input("Choose a noun: ").lower()
                noun2 = input("Choose another noun: ").lower()
                noun3 = input("And again, choose another noun: ").lower()
                verb = input("Choose a verb: ").lower()
                print()
                print(
                    "THE MYSTERY OF THE VANISHING SATELLITES",
                    "The space agency '" + name + "' faced a puzzling crisis: ",
                    "their satellites around " + planet + " were vanishing without a trace. ",
                    "Leading the investigation was Dr. " + name2 + ", ",
                    "a(n) " + adjective + " scientist known for solving the most baffling space mysteries.",
                    "The only clue was a series of " + adjective2 + " signals intercepted moments before each disappearance.",
                    "Believing these signals to be key,",
                    "Dr. " + name2 + " and their team embarked on a daring mission aboard the spacecraft '" + name3 + "',",
                    "equipped with a(n) " + noun + " and a(n) " + noun2 + ", to unravel the mystery.",
                    "What they discovered was a hidden " + noun3 + " with the power to " + verb + " matter,",
                    "guarded by an ancient alien civilization.",
                    sep="\n")
            print()
            story_6()
            print()
            print("Type roll once more, and let's catapult into our comedic cosmos ",
                  "with the grace of a gazelle galloping through gravity. ",
                  "Who knows, " + user_name + "? This roll might just be the one that writes us into the annals of astral hilarity!",
                  sep="\n")
            user_input = input("Type 'roll' to continue or 'quit' to exit: ")

        else:
            print("Invalid")

    elif user_input.lower() == "quit":
        print("Roll the credits!")  # make better obviously
        break

    else:
        print("Ah, attempting to communicate with the celestial beings using \"" + user_input + "\".")
        print("A bold strategy!",
              "Unfortunately, the intergalactic translators are currently tuned to 'dice' frequencies.",
              "Try 'roll' to ensure we don't accidentally send a love poem to a black hole.",
              sep="\n")
        user_input = input("They're known to be quite clingy. ")
