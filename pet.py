


class Pet:
    def __init__(self, name, pet_type="dog"):
        self.name = name
        self.pet_type = pet_type
        self.tricks = []
        self.energy = 100

    def eat(self):
        print(f"{self.name} is eating. Yum!")
        self.energy = min(100, self.energy + 15)

    def play(self):
        print(f"{self.name} is playing happily!")
        self.energy = max(0, self.energy - 20)

    def sleep(self):
        print(f"{self.name} is taking a nap...")
        self.energy = min(100, self.energy + 25)

    def train(self, trick):
        print(f"{self.name} learned a new trick: {trick}!")
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

    def get_status(self):
        print(f"\n📊 Status of {self.name}")
        print(f"Pet type: {self.pet_type}")
        print(f"Energy level: {self.energy}")
        print(f"Number of tricks: {len(self.tricks)}")
