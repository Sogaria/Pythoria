import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
randNum = random.randint(0, len(friends)-1)

print(friends[randNum])

random.shuffle(friends)
print(friends[0])