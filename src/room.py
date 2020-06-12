# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []
        # or should n e s w be none and adv file making the decision based on the room name?
    def __str__(self):
        return f"{self.name}: {self.description}. In this area you see {self.items}"

    # def get_items(self):

