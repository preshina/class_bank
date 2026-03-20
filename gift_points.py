# Add a method gift_points(amount, friends_list) where:

# friends_list is a list of Player objects

# Subtract amount from self.points for each friend

# Add amount to each friend’s points

# If not enough points, print "Not enough points for gifting" and stop gifting.


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def gift_points(self, amount, friends_list):
        total_needed = amount * len(friends_list)

        if self.points < total_needed:
            print("Not enough points for gifting")
            return

        self.points -= total_needed

        for friend in friends_list:
            friend.points += amount


p1 = Player("Hari", 100)
p2 = Player("Ram", 10)
p3 = Player("Sita", 5)

p1.gift_points(20, [p2, p3])
print(p1.points, p2.points, p3.points)
