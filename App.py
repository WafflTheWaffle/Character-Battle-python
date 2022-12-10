import time

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
time.sleep(1)
HAMSTER["hp"] = HAMSTER["hp"] + 20
print(HAMSTER["hp"])
time.sleep(1)
print(hamster_rival)
print(hamster_rival["hp"])
hamster_rival["hp"] = hamster_rival["hp"] + 20
print(hamster_rival["hp"])
time.sleep(1)


# This code for enemy attack is not working right now.
def enemy_attack():
    if hamster_rival["hp"] < 0:
        exit

    HAMSTER["hp"] = HAMSTER["hp"] - 10
    print("\nThe current hamster hp is now")
    print(HAMSTER["hp"])


def attack():
    if HAMSTER["hp"] < 0:
        exit

    if hamster_rival["hp"] < 0:
        hamster_rival["hp"] = 0
    user_attack = input("Do you want to attack? ")
    user_attack = str(user_attack)
    if user_attack != "y":
        print("What a coward!")
    else:
        hamster_rival["hp"] = hamster_rival["hp"] - 20
    print("Great! ", end='')
    print("The current hamster rival hp is now ", end='')
    print(hamster_rival["hp"])


time.sleep(1)
while hamster_rival["hp"] > 0:
    attack()

enemy_attack()
print(HAMSTER["hp"])
if HAMSTER["hp"] <= 0:
    print("Game Over.")

if hamster_rival["hp"] <= 0:
    print("You Defeated The Hamster Rival!")
