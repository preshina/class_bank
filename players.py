class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def add_points(self, amount):
        self.points += amount

    def send_points(self, amount, other_player):
        if amount <= self.points:
            self.points -= amount
            other_player.points += amount
        else:
            print("Not enough points")


p1 = Player("hari", 200)
p2 = Player("raj", 300)
p1.add_points(200)
p1.send_points(300, p2)
print(p1.points)
print(p2.points)
