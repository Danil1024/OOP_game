from models import *


def get_scores(player_obj):
    with open('scores.txt', 'a') as score:
        score.write(
            f'Player - {player_obj.name}, scored: {player_obj.score} points\n')


def get_player_instance():
    user_name = input('Enter your name: ')
    while not user_name:
        user_name = input('Enter your name: ')
    choice = input('Enter start for start the game: ')
    while choice != 'start':
        choice = input('Enter start for start the game: ')
    return Player(user_name)


def print_rules():
    print(RULES)


def get_enemy_instance(level=1):
    return Enemy(level)


def play():
    print_rules()
    player = get_player_instance()
    enemy = get_enemy_instance()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)

        except EnemyDown:
            player.score += 5
            enemy = get_enemy_instance(enemy.level + 1)

        except GameOver:
            get_scores(player)
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye')
