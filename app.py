player = {"Name": "asd", "Health": 100, "Heal": 16, "Attack": 10}
monster = {"Name": "Jack", "Health": 100, "Attack": 10}

print(player)
print(monster)

while True:
    print("---" * 10)
    print(f'{player["Name"]} has {player["Health"]} HP')
    print(f'{monster["Name"]} has {monster["Health"]} HP')
    print("1) Attack")
    print("2) Heal")

    player_move = input(">")

    print(player_move)
    if player_move == "1":
        monster["Health"] -= player["Attack"]
        player["Health"] -= monster["Attack"]
    elif player_move == "2":
        player["Health"] = player["Health"] + player["Heal"] - monster["Attack"]
    else:
        print("Invalid Choice")
