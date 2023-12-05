import random

class PasswordGenerator:
    def __init__(self):
        self.special_characters = ["$", "#", "!", "@", "*"]

    def generate(self, word):
        special_character = random.choice(self.special_characters)
        number = random.randint(1, 999)
        password = word + special_character + str(number)
        return password