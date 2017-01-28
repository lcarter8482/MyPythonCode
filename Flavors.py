import Epic

ratings = []
flavors = ["Vanilla", "Chocolate", "Strawberry", "Bacon"]

for flavor in flavors:
    rating = Epic.userString("Rate %s from 1 to 5:" % flavor)
    ratings.append("%s rated as a %s" % (flavor, rating))
print ratings