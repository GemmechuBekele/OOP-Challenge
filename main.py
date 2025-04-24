from pet import Pet
import time


def loading(action, petName=""):
    """Simulate loading time for pet actions."""
    if action == "teach":
        print(f"Teaching {petName} the new trick", end="")
    else:
        print(f"{petName} is {action}ing", end="")
    for _ in range(3):
        print(".", end="")
        time.sleep(0.5)
    print("")
    time.sleep(1)


# Main program starts here
print("==============================================")
print("Welcome to the Pet Simulator!")
print("You can create a pet and interact with it.")
print("Let's get started!")
name = input("Please enter the name of your pet: ")

userPet = Pet(name)
print("==============================================")
print(f"🐶 Congratulations! You have created a pet named {userPet.name}.")
time.sleep(2)
print("Now, let's see what you can do with your pet.")
time.sleep(2)

while True:
    print("\n==============================================")
    print("Available options:")
    print("1. 🍖 Feed your pet")
    print("2. ⚽ Play with your pet")
    print("3. ✍️  Teach your pet a trick")
    print("4. 📃 Check your pet's status")
    print("5. 😴 Allow your pet to sleep")
    print("6. 📃 Display all tricks your pet knows")
    print("7. 🚪 Exit")
    print("==============================================")

    try:
        userChoice = int(input("Please choose an option (1-7): "))
        if userChoice < 1 or userChoice > 7:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        time.sleep(2)
        continue

    if userChoice == 1:
        loading("feed", userPet.name)
        userPet.eat()
        userPet.get_status()

    elif userChoice == 2:
        loading("play", userPet.name)
        userPet.play()
        userPet.get_status()

    elif userChoice == 3:
        trick = input(
            "🎃 Please enter the trick you want to teach your pet: ").strip()
        if not trick:
            print("You didn't enter a trick. Please try again.")
        elif len(trick) > 20:
            print("Trick name is too long. Please keep it under 20 characters.")
        elif len(trick) < 3:
            print(
                "Trick name is too short. Please provide a name with at least 3 characters.")
        elif not trick.isalpha():
            print("Trick name should only contain letters.")
        elif trick in userPet.tricks:
            print(f"{userPet.name} already knows this trick!")
        else:
            loading("teach", userPet.name)
            userPet.train(trick)
            userPet.get_status()
        time.sleep(2)

    elif userChoice == 4:
        userPet.get_status()

    elif userChoice == 5:
        loading("sleep", userPet.name)
        userPet.sleep()
        time.sleep(2)
        userPet.get_status()

    elif userChoice == 6:
        userPet.show_tricks()
        time.sleep(2)

    elif userChoice == 7:
        print("Thank you for using the Pet Simulator!")
        break

# Simulate closing the simulator
print("Closing the Pet simulator", end="")
for _ in range(3):
    print(".", end="")
    time.sleep(1)
print("\nGoodbye! 🐾")

# >>>>>>> 
