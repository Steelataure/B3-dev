import random

class Operation():
    def __init__(self):
        pre_number = random.randint(1,500)
        self.pre_number = pre_number

        post_number = random.randint(1,500)
        self.post_number = post_number

        operateur = ["+", "-", "*"]
        self.operateur = operateur

        self.operateur_choice = random.choice(self.operateur)
        operateur_choice = self.operateur_choice

        self.LOSS = None

        self.generate_operation()

    def generate_operation(self):
        all_operation = str(self.pre_number) + self.operateur_choice + str(self.post_number)
        return all_operation

