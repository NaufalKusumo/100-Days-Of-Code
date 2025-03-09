import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randFriend = random.randint(0, len(friends) - 1)
print(friends[randFriend])
