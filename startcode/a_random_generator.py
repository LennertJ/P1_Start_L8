import random
voorvoegsels = ["big","small","electric","happy","angry","sneaky","stong"]
achtervoegsels = ["guardian","watcher","coder","ninja","gamer","knight","sorcerer","rogue"]
usernames = []

for i in range(10):
    voorvoegsel = random.choice(voorvoegsels)
    achtervoegsel = random.choice(achtervoegsels)
    usernames.append(voorvoegsel + " " + achtervoegsel)

print("10 random usernames: ")
for username in usernames:
    print(username)