from random import randint


def pri_winner(name1, name2, win):
    print('$$$' * 10)
    if win == "p":
        print(f'{name2} killed {name1}')
        print("Another Monster Arrives")
    if win == "m":
        print(f'{name1} finally defeated {name2}')
    print('$$$' * 10)


def generate_monster():
    f = open("Monsters Data.txt", "r")
    monster_id = randint(0, 9)

    for line in f:
        if line[0] == str(monster_id):
            data = line.split()
            new_monster = {"Name": data[1],
                           "Health": int(data[2]),
                           "Attack": int(data[3]),
                           "Attack spread": int(data[4])}

    f.close()
    return new_monster


def show_leaderboard():
    f = open("Leader Board.txt", "r")
    file = f.read()
    f.close()

    print("&" * 30)
    print(file)
    print("&" * 30)


def sort_second(val):
    return -1 * val[1]


def update_leaderboard(name, monster_killed):
    f = open("Leader Board.txt", "r")
    data = []
    for line in f:
        d = line.split(' ')
        data.append((d[2], int(d[5].rstrip())))
    f.close()

    data.append((name, monster_killed))
    data.sort(key=sort_second)

    f = open("Leader Board.txt", "w")
    it = min(len(data), 10)
    for i in range(0, it):
        if i != it - 1:
            f.write(f'{i+1}. Name: {data[i][0]} Monster killed: {data[i][1]}\n')
        else:
            f.write(f'{i+1}. Name: {data[i][0]} Monster killed: {data[i][1]}')
    f.close()


def main_game():
    player = {"Name": "asd", "Health": 100, "Heal": 16, "Attack": 10}
    monster = generate_monster()

    print("Enter Player Name")
    player["Name"] = input(">")

    player_status = "lives"
    monster_status = "lives"
    monster_killed = 0

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
                player["Health"] -= (monster["Attack"] + randint(0, monster["Attack spread"]))
            else:
                monster_status = "dead"
        elif player_move == "2":
            monster_attack = (monster["Attack"] + randint(0, monster["Attack spread"]))
            player["Health"] = player["Health"] + player["Heal"] - monster_attack
        elif player_move == "3":
            game_in_progress = False
        else:
            print("Invalid Choice")

        if player["Health"] <= 0:
            player_status = "dead"

        if monster_status == "dead":
            monster_killed += 1
            pri_winner(monster["Name"], player["Name"], "p")
            monster = generate_monster()
            print(f'{monster["Name"]} came to fight you.')
            monster_status = "lives"

        if player_status == "dead":
            game_in_progress = False
            pri_winner("Monsters", player["Name"], "m")
            update_leaderboard(player["Name"], monster_killed)


game = True

while game:
    print("---" * 10)
    print("1) Start Game")
    print("2) Leader Board")
    print("3) Exit Game")
    main_game_input = input(">")

    if main_game_input == "1":
        main_game()
    elif main_game_input == "2":
        show_leaderboard()
    elif main_game_input == "3":
        game = False
    else:
        print("Invalid Choice")
