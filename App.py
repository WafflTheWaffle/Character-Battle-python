import random

HAMSTER = {
    "hp": 27,
    "color": "Mint",
    "speed": "INFINITE",
    "favorite food": "human and penut",
    "Hobby": "runs on piano",
    "attack": 7

}
hamster_rival = {
    "hp": 34,
    "color": "gold_brown",
    "speed": 0,
    "food": "none",
    "hobby": "getting_eaten",
    "name": "penut_shell"
}

print(HAMSTER)
print(HAMSTER["hp"])

HAMSTER["hp"] = HAMSTER["hp"] + 20
print(HAMSTER["hp"])
print(hamster_rival)
print(hamster_rival["hp"])
hamster_rival["hp"] = hamster_rival["hp"] + 20
print(hamster_rival["hp"])


def enemy_attack():
    user_attack = random.choice(0, 1)
    if user_attack != 1:
        print("your enemy chose to not attack")
    else:
        HAMSTER["hp"] = HAMSTER["hp"] - 10
    print("Great! ", end='')
    print("The current hamster hp is now ", end='')
    print(HAMSTER["hp"])


def attack():
    if hamster_rival["hp"] < 0:
        hamster_rival["hp"] = 0
    user_attack = input("Do you want to attack? ")
    user_attack = str(user_attack)
    if user_attack := "Yes":
        hamster_rival["hp"] = hamster_rival["hp"] - 20
    else:
        print("What a coward!")

    print("\nThe current hamster rival hp is now")
    print(hamster_rival["hp"])


while (hamster_rival["hp"] > 0):
    attack()
