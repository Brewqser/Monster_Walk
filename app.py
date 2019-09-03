from random import randint


def pri_winner(name):
    print('$$$' * 10)
    print(f'{name} wins')
    print('$$$' * 10)


def main_game():
    player = {"Name": "asd", "Health": 100, "Heal": 16, "Attack": 10}
    monster = {"Name": "Jack", "Health": 100, "Attack": 10}

    print("Enter Player Name")
    player["Name"] = input(">")

    player_status = "lives"
    monster_status = "lives"

    game_in_progress = True
    while game_in_progress:
        print("---" * 10)
        print(f'{player["Name"]} has {player["Health"]} HP')
        print(f'{monster["Name"]} has {monster["Health"]} HP')
        print("1) Attack")
        print("2) Heal")
        print("3) Exit Round")

        player_move = input(">")

        if player_move == "1":
            monster["Health"] -= player["Attack"]
            if monster["Health"] > 0:
                player["Health"] -= (monster["Attack"] + randint(0, 9))
            else:
                monster_status = "dead"
        elif player_move == "2":
            player["Health"] = player["Health"] + player["Heal"] - (monster["Attack"] + randint(0, 9))
        elif player_move == "3":
            game_in_progress = False
        else:
            print("Invalid Choice")

        if player["Health"] <= 0:
            player_status = "dead"

        if monster_status == "dead":
            game_in_progress = False
            # generate new monster

        if player_status == "dead":
            game_in_progress = False
            pri_winner("Monsters")
            # check Leader Boards
            # end game


game = True

while game:
    print("---" * 10)
    print("1) Start Game")
    print("2) Leader Boards")
    print("3) Exit Game")
    main_game_input = input(">")

    if main_game_input == "1":
        main_game()

    elif main_game_input == "2":
        # show Leader Boards
        print("written soon")

    elif main_game_input == "3":
        game = False

    else:
        print("Invalid Choice")

